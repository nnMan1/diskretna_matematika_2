import networkx as nx
from matplotlib import pyplot as plt

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 4 , 3])

G.add_edge(1, 2)
G.add_edges_from([(2, 3), (3, 1)])

nx.draw(G, with_labels=True)
plt.savefig('graf.png')
# plt.figure()
plt.cla()

print(f'Graf ima {G.number_of_edges()} grana i {G.number_of_nodes()} cvorova.')

G.clear() 
G.add_node('Podgorica', br_stanovnika=150000)
G.add_nodes_from([('Kolasin', {'br_stanivnika': 5000}), 'Berane', 'Bar', 'Bijelo Polje'])

G.add_edges_from([
    ('Podgorica', 'Kolasin', {'rastojanje': 42, 'tip': 'autoput'}),
    ('Kolasin', 'Berane', {'rastojanje': 50, 'tip': 'lokalni'}),
    ('Berane', 'Bijelo Polje'),
    ('Bijelo Polje', 'Kolasin'),
    ('Podgorica', 'Bar'),
    ('Bar', 'Budva')
])

pos = {
    'Podgorica': (0, 0),
    'Kolasin': (0, 1),
    'Berane': (0.5, 1.5),
    'Bijelo Polje': (-0.5, 0.5),
    'Bar': (0, -1),
    'Budva': (-1, 1)
}

options = {
    'with_labels': True,
    'font_size': 20,
    'node_size': 2000,
    'node_color': 'white',
    'linewidths': 5,
    'edgecolors':'black',
    'width': 3
}
G.nodes['Berane']['br_stanovnika'] = 20000

print(G.nodes.data())
print("Infor o PG", G.nodes['Podgorica'])




# print(G.edges.data())
# print('Info o grani PG-KL', G.edges[('Podgorica', 'Kolasin')])

# nx.draw_networkx(G, 
#                  pos=pos, 
#                  **options
#                  )
# plt.savefig('graf.png')