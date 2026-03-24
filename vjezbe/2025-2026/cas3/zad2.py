import networkx as nx
import matplotlib.pyplot as plt

# graph = nx.path_graph(5)
# graph = nx.cycle_graph(10)
# graph = nx.complete_graph(5)
# graph = nx.complete_bipartite_graph(5, 6)
graph = nx.petersen_graph()

nx.draw(graph, with_labels=True)
plt.show()