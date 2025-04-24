import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_edges_from(['AB', 'AE', 'CB', 'AC', 'BD', 'DE', 'DA', 'DC', 'DB', 'CF', 'EF'])

colors = nx.coloring.greedy_coloring(g, strategy="largest_first")
print(colors)

nx.draw(g, with_labels=True, node_color=list(colors.values()), node_size=500, font_size=16)
plt.show()