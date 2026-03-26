import networkx as nx
import matplotlib.pyplot as plt

def ucitaj_graf():
    n = int(input("Unesite broj cvorova: "))
    m = int(input("Unesite broj grana: "))

    G = nx.Graph() 
    # G = nx.DiGraph() #ako zelimo usmjereni graf

    for i in range(n):
        G.add_node(f"{i}")

    for i in range(m):
        line = input() #ucitava citavu liniju
        # susjedi = line.split(" ")
        x, y = line.split(" ")
        G.add_edge(x, y)

    return G

def dfs(G, u, visited, label):

    visited[u] = label

    for v in G[u]: 
        if visited[v] == -1:
            dfs(G, v, visited, label)

def komponente_povezanosti(G):

    komponente = {x: -1 for x in G.nodes}

    label = 0
    for u in G.nodes:
        if komponente[u] == -1:
            dfs(G, u, komponente, label)
            label += 1

    return label, komponente

def najveca_komponenta(G):

    br_komponenti, komponente = komponente_povezanosti(G)
    velicina = [0 for _ in range(br_komponenti)]

    max_komponenta = 0

    for u in G.nodes:
        velicina[komponente[u]] += 1

        if velicina[komponente[u]] > velicina[max_komponenta]:
            max_komponenta = komponente[u]

    return [v for v in G.nodes if komponente[v] == max_komponenta]
        
def ciklican(G):

    def ciklican_dfs(G, u, visited, parent):

        visited[u] = True

        for v in G[u]: 
            if visited[v] == False:
                ciklican_dfs(G, v, visited, u)
            elif v != parent:
                return True
            
        return False

    visited = {u: False for u in G.nodes}

    for u in G.nodes:
        if not visited[u] and ciklican_dfs(G, u, visited, -1):
            return True
    
    return False

def bipartitan(G):

    def dfs_bipartitan(G, u, partition, label):

        partition[u] = label

        for v in G[u]:
            if partition[v] == -1:
                if not dfs_bipartitan(G, v, partition, 1 - label):
                    return False
            elif partition[v] == partition[u]:
                return False
            
        return True
    
    partition = {u: -1 for u in G.nodes}

    for u in G.nodes:
        if partition[u] == -1 and not dfs_bipartitan(G, u, partition, 0):
            return False
        
    print(partition)
    
    return True

def dfs_edges(G):

    edges = []
    visited = {u: False for u in G.nodes}

    def dfs(u, parent, t):
        visited[u] = True
        if parent != -1:
            edges.append((parent, u, {"t": t}))

        for v in G[u]:
            if not visited[v]:
                t = dfs(v, u, t+1)

        return t
    
    t = 0
    for u in G.nodes:
        if not visited[u]:
            t = dfs(u, -1, t)

    return edges

def draw_dfs_tree(G):

    dfs_tree = dfs_edges(G)

    pos = nx.spring_layout(G)

    nx.draw(G, pos=pos, with_labels=True)
    plt.show()

    tmp = []

    for edge in dfs_tree: 

        tmp.append(edge)

        fix, axes = plt.subplots(1, 2, figsize=(12, 6))

        ax = axes[0]
        nx.draw_networkx(G, pos=pos, ax=ax, with_labels=True, edge_color="g")

        ax = axes[1]
        tree = nx.DiGraph()
        tree.add_edges_from(tmp)
        edge_labels = nx.get_edge_attributes(tree, 't')
        # edge_labels[('0', '1')] = "DM2"
        nx.draw_networkx_nodes(G, pos=pos, ax=ax, nodelist=G.nodes)
        nx.draw_networkx_labels(G, pos=pos, ax=ax, labels={n: n for n in G.nodes})
        nx.draw_networkx_edges(tree, pos=pos, ax=ax, edge_color="r")
        nx.draw_networkx_edge_labels(tree, pos=pos, ax=ax, edge_labels=edge_labels)      

        plt.show()

G = ucitaj_graf()
u = input("u: ")

br_komponenti, komponente = komponente_povezanosti(G)
print("Komponenta(u) = ", [v for v in G.nodes if komponente[v] == komponente[u]])
# print("Broj komponenti: ", len(set(komponente.values())))
print("Broj komponenti: ", br_komponenti)
print("Najveca komponenta: ", najveca_komponenta(G))
print("Velicina najvece komponente: ", len(najveca_komponenta(G)))
print("Ciklican: ", ciklican(G))
print("Bipartitan: ", bipartitan(G))
print("DFS tree: ", dfs_edges(G))

draw_dfs_tree(G)
