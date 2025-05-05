import networkx as nx

G = nx.Graph()

G.add_node(1, back_par= 0)

G.add_edges_from([
    (1, 3), (3, 6), (3, 5), (5, 7), (5, 13), (6, 2), (2, 4), (4, 10), (2, 8), (1, 6),
    (1, 9), (9, 11), (11, 12), (12, 9), (3, 8), (7, 3), (13, 3), (5, 14), (14, 15), (15, 16), (16, 14)
])

nx.draw_networkx(G, with_labels=True)

def dfs_find_bridges(G):

  timer = 0
  visited = [False for _ in range(len(G.nodes) + 1)]
  tin = [-1 for _ in range(len(G.nodes) + 1)]
  tree_edges = []
  bridges = []

  back_edges_start = [0 for _ in range(len(G.nodes) + 1)]
  back_edges_end = [0 for _ in range(len(G.nodes) + 1)]

  def dfs(source, parent):
    nonlocal timer

    if visited[source]:
      if parent != -1 and tin[source] < tin[parent]:
        back_edges_end[source] += 1
        back_edges_start[parent] += 1
      return 0

    tin[source] = timer
    timer += 1

    visited[source] = True

    if parent != -1:
      tree_edges.append((source, parent))

    num_back_edges = 0

    for v in G[source]:
      if v != parent:
        num_back_edges += dfs(v, source)

    num_back_edges += back_edges_start[source]
    num_back_edges -= back_edges_end[source]

    timer += 1

    if parent != -1 and num_back_edges == 0:
      bridges.append((parent, source))

    return num_back_edges

  for u in G.nodes:
    if visited[u] == False:
      dfs(u, -1)

  return bridges


bridges = dfs_find_bridges(G)
print(bridges)

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, G.edges, edge_color="black")
nx.draw_networkx_edges(G, pos, bridges, edge_color="red")

def dfs_articulation_points(G):
    """
    G: adjacency list, e.g.:
       G[u] = list of neighbors for node u.
       We assume G is 0- or 1-indexed consistently.
    Returns: a list (or set) of all articulation points in G.
    """

    # We'll assume nodes are labeled from 1..N if len(G.nodes) = N, or 0..N-1 if that is easier.
    # If G.nodes is a dictionary-like structure, you might do something slightly different.
    # But the approach is the same.
    n = len(G.nodes)  # Number of nodes

    visited = [False] * (n + 1)
    tin = [-1] * (n + 1)
    tmin = [-1] * (n + 1)

    # We don't necessarily need tout or back_edges arrays for articulation points.
    # We'll keep track of a global timer in a list so we can modify inside the nested function
    timer = [0]

    # We'll store articulation points in a set (avoid duplicates)
    articulation_points_set = set()

    def dfs(u, parent):
        visited[u] = True
        tin[u] = timer[0]
        tmin[u] = timer[0]
        timer[0] += 1

        children_count = 0  # number of children in DFS tree for root-check
        is_articulation = False  # track if 'u' meets articulation condition (non-root case)

        for v in G[u]:
            if v == parent:
                continue

            if not visited[v]:
                children_count += 1
                dfs(v, u)

                # After DFS on 'v', update low-link (tmin) for 'u'
                tmin[u] = min(tmin[u], tmin[v])

                # Non-root articulation condition:
                if parent != -1 and tmin[v] >= tin[u]:
                    is_articulation = True
            else:
                # v is already visited and is not the parent => back edge
                tmin[u] = min(tmin[u], tin[v])

        # Root articulation condition:
        # If u is the root of this DFS (parent == -1) and it has more than one child
        if parent == -1 and children_count > 1:
            is_articulation = True

        if is_articulation:
            articulation_points_set.add(u)

    # Run DFS on each node that hasn't been visited yet
    for node in G.nodes:
        if not visited[node]:
            dfs(node, -1)

    # Return the articulation points as a list (or you can keep as set)
    return list(articulation_points_set)


art_points = dfs_articulation_points(G)
print(art_points)

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, G.edges, edge_color="black")
nx.draw_networkx_nodes(G, pos, art_points, node_color="red")
