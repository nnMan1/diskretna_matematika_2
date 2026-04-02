import networkx as nx

def read_graph():
    n = int(input("Unesite broj cvorova: "))
    m = int(input("Unesite broj grana: "))

    G = nx.Graph()

    for i in range(m):
        line = input()
        a, b = line.split(" ")
        
        G.add_edge(a, b)

    return G

def read_graph_from_file(f):

    with open(f) as fajl:

        n = int(fajl.readline())
        m = int(fajl.readline())

        G = nx.Graph()

        for i in range(m):
            line = fajl.readline().strip()
            a, b = line.split(" ")
            
            G.add_edge(a, b)

    return G