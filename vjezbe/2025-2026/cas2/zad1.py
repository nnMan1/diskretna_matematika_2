import networkx as nx
import matplotlib.pyplot as plt

# def print_two_numbers(x, y):
#     print(x, y)

# args = {
#     "y": 9,
#     "x": 7
# }

# print_two_numbers(**args)
# exit(0)

G = nx.Graph() #nesumjeren bez vis grana 
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)

# G.add_edge(1, 2)
# G.add_edge(1, 3)

print("Nodes: ", G.nodes)
print("Edges: ", G.edges)

G.add_edges_from([(1, 4), (3, 2)])

print("Nodes: ", G.nodes)
print("Edges: ", G.edges)

G.add_nodes_from([
    "Kolasin", 
    ("Podgorica", {"populacija": 150000}), 
    ("Berane", {"populacija": 20000, "lat": 43.145343, "long": 44.32324232})])

print("Nodes: ", G.nodes)
print("Edges: ", G.edges)

G.add_edge("Berane", "Andrijevica")   #cvor 20 se dodaje automatski
print("Nodes: ", G.nodes)
print("Edges: ", G.edges)

print(f"Graf G sadrzi {G.number_of_nodes()} cvorova i {G.number_of_edges()} grana.")

# nx.draw(G, with_labels=True)
# plt.show()

putevi = G
zeljeznice = nx.Graph() 

zeljeznice.add_edges_from([(1, 2, {"duzina": 50}), (2, 3), (3, 1)])

# pos = {
#     1: (0, 1),
#     2: (1, 1),
#     3: (1, 0)
# }
pos = nx.spring_layout(putevi)
options = {
    "with_labels": True, 
    "pos": pos, 
    "node_shape": '*',
    "node_color": "purple",
    "font_color": "black",
    "node_size": 500
}

# nx.draw(putevi, pos=pos)
# nx.draw(zeljeznice, 
#         with_labels=True, 
#         pos=pos, 
#         node_color='red', 
#         node_shape='*',
#         edge_color="purple",
#         font_color="white",
#         node_size=500)
# nx.draw_networkx_nodes(G, pos=pos)
# nx.draw_networkx_edges(G, pos=pos, edge_color="green")
# nx.draw_networkx_labels(putevi, pos=pos, font_color="orange")

# nx.draw(putevi, edge_color="green", **options)
# nx.draw(zeljeznice, edge_color="red", **options)

G.add_node("Niksic", populacija=60000)

for node in G.nodes:
    print(node, G.nodes[node])

print(zeljeznice.edges[1, 2])