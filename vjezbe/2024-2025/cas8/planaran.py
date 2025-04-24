import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_edges_from(['AB', 'AE', 'CB', 'AC', 'BD', 'DE', 'DA', 'DC', 'DB', 'CF', 'EF'])

print(nx.is_planar(g))
nx.draw(g, with_labels=True)
plt.show()

g.add_edge('E', 'C')
g.add_edge('B', 'E')
print(nx.is_planar(g))
nx.draw(g, with_labels=True)
plt.show()

