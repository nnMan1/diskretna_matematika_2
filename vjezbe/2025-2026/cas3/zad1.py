import networkx as nx
import matplotlib.pyplot as plt

PMF = nx.Graph(opis = "Prirodno-matematicki fakultet")

PMF.add_node("Sanja", tip="profesor")
PMF.add_nodes_from([
    ("Ana", {"tip": "student", "godina_upisa": 2025}),
    ("Marko", {"tip": "student", "godina_upisa": 2024})
])
PMF.add_node("Diskretna matematika", tip="predmet")
PMF.add_node("Analiza", tip="predmet")


PMF.add_edges_from([
    ["Ana", "Diskretna matematika", {"slusa": 3}],
    ["Ana", "Analiza"],
    ["Marko", "Analiza"]
])

print("Cvorovi: ", PMF.nodes)
print("Grane: ", PMF.edges)
print("Grane['Ana']: ", PMF['Ana'])
print("Atributi[Ana]: ", PMF.nodes['Ana'])
print("Adtibuti[Ana-Diskretna matematika]: ", PMF.edges["Ana", "Diskretna matematika"])
print("PMF.adj: ", PMF.adj)
print("Ana['Diskrenta matematika]:", PMF.adj["Ana"]["Diskretna matematika"])
exit(0)


pos = nx.spring_layout(PMF)

# temp = []
# for node in PMF.nodes:
#     if node['tip'] == 'sudent':
#         temp.append(node)

temp = [node for node in PMF.nodes if PMF.nodes[node]['tip'] == 'student']
print(temp)

nx.draw_networkx_nodes(PMF, 
                       pos=pos, 
                       nodelist=[node for node in PMF.nodes if PMF.nodes[node]['tip'] == 'student'],
                       node_color='red'
                       )


nx.draw_networkx_nodes(PMF, 
                       pos=pos, 
                       nodelist=[node for node in PMF.nodes if PMF.nodes[node]['tip'] == 'predmet'],
                       )

nx.draw_networkx_labels(PMF,
                        pos=pos,
                        labels={node: f'Student_{node}' for node in PMF.nodes if PMF.nodes[node]['tip'] == 'student'}
                        )

# labels = {}
# for node in G.nodes:
#     if G.nodes[node]['tip'] == 'predmet':
#         labels[node] = f"Predmet_{node}"

# labels = {node: f"Predmet_{node}" for node in PMF.nodes if PMF.nodes[node]['tip'] == 'predmet'}

nx.draw_networkx_labels(PMF,
                        pos=pos,
                        labels={node: f'Predmet_{node}' for node in PMF.nodes if PMF.nodes[node]['tip'] == 'predmet'}
                        )

plt.show()

PMF.clear()
nx.draw(PMF, with_labels=True)
plt.show()