#Nalazenje mostova u grafu

import networkx as nx
import matplotlib.pyplot as plt
from tools import read_graph_from_file

def find_bridges(G):
    timer = 0
    bridges = []
    visited = {u: False for u in G}
    back_edges_start = {u: 0 for u in G}
    back_edges_end = {u: 0 for u in G}
    tin = {u: -1 for u in G}
    tree_edges = []
    back_edges = []

    def dfs(source, parent):

        nonlocal timer

        if visited[source]:
            if parent != -1 and tin[source] < tin[parent]:
                back_edges.append((source, parent))
                back_edges_start[parent] += 1
                back_edges_end[source] += 1
            return 0
        
        if parent != -1:
            tree_edges.append((source, parent))
        
        visited[source] = True
        tin[source] = timer
        timer += 1
        
        num_back_edges = 0

        for v in G[source]:
            if v != parent:
                num_back_edges += dfs(v, source)

        timer += 1
        num_back_edges += back_edges_start[source]
        num_back_edges -= back_edges_end[source]

        if num_back_edges == 0 and parent != -1:
            bridges.append((parent, source))

        return num_back_edges
    
    for u in G:
        if not visited[u]:
            dfs(u, -1)

    return bridges, tree_edges, back_edges

G = read_graph_from_file("graph.txt")

pos = nx.spring_layout(G)
nx.draw(G, pos=pos, with_labels=True)
bridges, tree_edges, back_edges = find_bridges(G)
nx.draw_networkx_edges(G, pos=pos, edgelist=bridges, edge_color="#55AA65")

plt.show()