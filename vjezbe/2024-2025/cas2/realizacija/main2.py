import networkx as nx
from matplotlib import pyplot as plt

T = nx.Graph()
T.add_nodes_from([7, 9, 6, 4])

G = nx.path_graph(5)

T.add_nodes_from(G.nodes)
T.add_edges_from(G.edges)



print(T.adj)
print(list(T.nodes))
print(list(T.edges))

ax = plt.subplot(121)
nx.draw(T, ax=ax, with_labels=True)
plt.axis('on')

T.remove_node(1)
ax = plt.subplot(122)
nx.draw(T, ax=ax, with_labels=True)
plt.axis("on")                        


plt.savefig('graf.png')
