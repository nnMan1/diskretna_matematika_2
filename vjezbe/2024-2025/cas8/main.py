import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_edges_from(['AB', 'AE', 'CB', 'AC', 'BD', 'DE', 'DA', 'DC', 'DB', 'CF', 'EF'])

path = list(nx.eulerian_path(g))

pos = nx.spring_layout(g)
nx.draw_networkx_nodes(g, pos)
nx.draw_networkx_edges(g, pos)
nx.draw_networkx_labels(g, pos)

path_graph = nx.DiGraph()
path_graph.add_edges_from(path)
nx.draw_networkx_edges(path_graph, pos, edge_color="red")
print( {e: i for i, e in enumerate(path)})
nx.draw_networkx_edge_labels(path_graph, pos, {e: i for i, e in enumerate(path)})

plt.show()