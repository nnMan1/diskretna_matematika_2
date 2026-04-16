import networkx as nx
import matplotlib.pyplot as plt
from tools import read_graph_from_file

def articulation_nodes(G):

    visited = {u: False for u in G}
    t_in = {u: -1 for u in G}
    t_min = {u: -1 for u in G}
    timer = 0
    articulation_nodes_list = []

    def dfs(u, parent):

        nonlocal timer

        visited[u] = True
        t_in[u] = timer
        t_min[u] = timer
        timer += 1
        is_articulation = False
        children_count = 0

        for v in G[u]:
            if v == parent:
                continue

            if not visited[v]:
                dfs(v, u)
                children_count += 1
                t_min[u] = min(t_min[u], t_min[v])
                if parent != -1 and t_min[v] >= t_in[u]:
                    is_articulation = True
            else:
                t_min[u] = min(t_min[u], t_in[v])

        if parent == -1 and children_count > 1:
            is_articulation = True

        if is_articulation:
            articulation_nodes_list.append(u)

    for u in G:
        if not visited[u]:
            dfs(u, -1)

    return articulation_nodes_list


G = read_graph_from_file("graph.txt")
print(articulation_nodes(G))

nx.draw(G, with_labels=True)
plt.show()