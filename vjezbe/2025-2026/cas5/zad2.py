import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([
    ("BA", "KL"),
    ("KL", "PG"),
    ("BA", "AN"),
    ("BP", "MK"),
    ("MK", "KL"),
    ("BA", "BP"),
    ("PG", "DG"),
    ("NK", "PL"),
    ("NK", "SN"),
    ("SN", "ZB")
])

komponente = list(nx.connected_components(G))
dfs_edges = list(nx.dfs_edges(G))

print(dfs_edges)

pos = nx.spring_layout(G)
nx.draw_networkx(G, pos=pos, with_labels=True)

colors = "rgbopc"

for i, c in enumerate(komponente):
    nx.draw_networkx_nodes(G, pos, c, node_color=colors[i])

nx.draw_networkx_edges(G, pos=pos, edgelist=dfs_edges, edge_color="y")
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels={e: i for i, e in enumerate(dfs_edges)})

plt.show()