import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph()
g.add_edges_from([(1, 2),
                  (2, 3),
                  (3, 1),
                  (2 ,4),
                  (3, 4),
                  (4 ,5)])

print(list(nx.strongly_connected_components(g)))

top_sort = nx.topological_sort(g)
print(list(top_sort))
nx.draw(g, with_labels=True)
plt.show()

# Dat je niz rijeci. Rijeci se sastoje od malih slova engleskog alfabeta.
# Da li je moguce naprviti permutaciju alfabeta,
# tako da po toj permutaciji rijeci budu leksikografski sortirane.
# Ako jeste, stapati poredak rijeci.

#banana
#kuska
#jabuka
#baba

# n -> b
# b -> k
# k -> j
