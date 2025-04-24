import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
# g.add_edges_from([(1, 3), (3, 6), (5, 7), (7, 3), (5, 1), (2, 6), (2, 8), (8, 3), (2, 4), (4, 10),(1, 9), (9, 11), (11, 12)])
# g.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 2), (2, 6), (6, 7), (7, 5), (5, 8), (8, 9), (9, 10), (10, 11), (11, 8), (8, 12), (12, 13), (13, 11), (11, 14)])   
g.add_edges_from(['AB', 'AE', 'CB', 'AC', 'BD', 'DE', 'DA', 'DC', 'DB', 'CF', 'EF'])

def is_eulerian(g):

    if not nx.is_connected(g):
        return False

    cnt = 0
    for u in g.nodes:
        if len(g[u]) % 2 == 1:
            cnt += 1

    return cnt == 0 or cnt == 2

def eulerian_path(g):

    if not is_eulerian(g):
        return []

    start_node = list(g.nodes)[0]

    for u in g.nodes:
        if len(g[u]) % 2 == 1:
            start_node = u
            break

    s = []
    out_deg = {u: len(g[u]) for u in g.nodes}
    traversed_edges = set()
    path = []

    def travel(source):

        s.append(source)

        if out_deg[source] == 0:
            path.append(source)
            s.pop()
            return


        for v in g[source]:
            if (v, source) not in traversed_edges:
                traversed_edges.add((source, v))
                traversed_edges.add((v, source))
                out_deg[u] -= 1
                out_deg[v] -= 1
                travel(v)

        s.pop()
        path.append(source)
    
    travel(start_node)
    return path

print(is_eulerian(g))

nx.draw_networkx(g, with_labels=True)
plt.show()

# print(list(nx.euler.eulerian_circuit(g)))
path = eulerian_path(g)
pos = nx.spring_layout(g)
nx.draw_networkx_nodes(g, pos)
nx.draw_networkx_edges(g, pos)
nx.draw_networkx_labels(g, pos)

path_graph = nx.DiGraph()
path_graph.add_edges_from(zip(path[:-1], path[1:]))
nx.draw_networkx_edges(path_graph, pos, edge_color="red")
print( {e: i for i, e in enumerate(zip(path[:-1], path[1:]))})
nx.draw_networkx_edge_labels(path_graph, pos, {e: i for i, e in enumerate(zip(path[:-1], path[1:]))})


plt.show()