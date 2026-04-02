import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from tools import read_graph, read_graph_from_file

colors = np.random.randint(0, 255, (100, 3)) #matrica dimenzija 100x3 random

def bfs(G, x):
    queue = []
    visited = {u: False for u in G.nodes}
    distance = {u: -1 for u in G.nodes}

    distance[x] = 0
    queue.append(x)
    visited[x] = True

    while len(queue) > 0:
          u = queue.pop(0)

          for v in G[u]:
            if not visited[v]:
                    visited[v] = True
                    distance[v] = distance[u] + 1
                    queue.append(v)
    
    return distance

def bipartite(G):
    distance = bfs(G, list(G.nodes)[0])
    for u, v in G.edges:
        if distance[u] % 2 == distance[v] % 2:
            return False
          
    return True

G = read_graph_from_file("graph.txt")

distance = bfs(G, 'BA')
print(distance)
print("Graf G ", ("jeste" if bipartite(G) else "nije"), "bipartitan") 

pos = nx.spring_layout(G)
nx.draw(G, pos=pos, with_labels=True)
colors = ["#00FF00", "blue", "green", "orange", "purple", "black"]


# for i in range(max(distance.values())):
#     nx.draw_networkx_nodes(G, 
#                            pos=pos, 
#                            nodelist=[u for u in G.nodes if distance[u] == i],
#                            node_color=colors[i])
# nx.draw(G, with_labels=True)
# plt.show()

print(list(nx.bfs_edges(G, 'BA')))
bfs_layers=list(nx.bfs_layers(G, 'BA'))

for i in range(max(distance.values())):
    nx.draw_networkx_nodes(G, 
                           pos=pos, 
                           nodelist=bfs_layers[i],
                           node_color=colors[i])
    
plt.show()