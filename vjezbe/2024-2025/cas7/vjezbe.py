import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_edges_from(['AB', 'AC', 'AM', 'AN', 'BC', 'BD', 'BL',
                  'DP', 'PR', 'RS', 'SD', 'DE', 'DJ', 'EJ',
                  'EF', 'EQ', 'QI', 'QH', 'HI', 'QF', 'IJ',
                  'IK', 'JK', 'KL', 'KM', 'LM', 'MN', 'LD'])

def is_euler(g):
    if not nx.is_connected(g):
        return False
    
    odd_deg_counter = 0
    for u in g.nodes:
        if len(g[u]) % 2 == 1:
            odd_deg_counter += 1
    
    return odd_deg_counter == 0 or odd_deg_counter == 2

def euler_paht(g):

    if not is_euler(g):
        return []
    
    start_node = list(g.nodes)[0]
    for u in g.nodes:
        if len(g[u]) % 2 == 1:
            start_node = u
            break

    node_deg = {u: len(g[u]) for u in g.nodes}
    traveled_edges = set()
    path = []

    def travel(source):

        if node_deg[source] == 0:
            path.append(source)
            return
    
        for v in g[source]:
            if (source, v) not in traveled_edges:
                traveled_edges.add((source, v))
                traveled_edges.add((v, source))

                node_deg[source] -= 1
                node_deg[v] -= 1

                travel(v)

        path.append(source)

    travel(start_node)
    return path


print(is_euler(g))
path = euler_paht(g)

pos = nx.spring_layout(g)
nx.draw_networkx_nodes(g, pos)
nx.draw_networkx_edges(g, pos)
nx.draw_networkx_labels(g, pos)

path_grpah = nx.DiGraph()

labels = {}
for i in range(1, len(path)):
    path_grpah.add_edge(path[i-1], path[i])
    labels[path[i-1], path[i]] = i

nx.draw_networkx_edges(path_grpah, pos, edge_color='red')

nx.draw_networkx_edge_labels(path_grpah, pos, labels)


plt.show()