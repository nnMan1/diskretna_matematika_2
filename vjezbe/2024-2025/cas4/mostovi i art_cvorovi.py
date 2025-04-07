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

  timer = 0
  visited = [False for _ in range(len(G.nodes) + 1)]
  tin = [-1 for _ in range(len(G.nodes) + 1)]
  tout = [-1 for _ in range(len(G.nodes) + 1)]
  tmin = [-1 for _ in range(len(G.nodes) + 1)]
  tree_edges = []
  articulation_points = []

  back_edges_start = [0 for _ in range(len(G.nodes) + 1)]
  back_edges_end = [0 for _ in range(len(G.nodes) + 1)]

  def dfs1(source, parent):
    nonlocal timer

    if visited[source]:
      return 
    
    is_articulation_point = False

    tin[source] = timer
    tmin[source] = timer
    timer += 1

    visited[source] = True

    if parent != -1:
      tree_edges.append((source, parent))

    num_back_edges = 0
    num_child = 0

    for v in G[source]:
      if v != parent:
        if !visited[v]:
            num_child += 1
            dfs1(v, source)
            tmin[source] = min(tmin[source], tmin[v])

        if tmin[v] >= tin[source]:
          is_articulation_point = True

    if is_articulation_point:
      articulation_points.append(source)

    timer += 1
    tout[source] = timer
    return num_child

  for u in G.nodes:
    if visited[u] == False:
      if dfs1(u, -1) > 1:
        articulation_points.append(u)

  return articulation_points


art_points = dfs_articulation_points(G)
print(art_points)

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, G.edges, edge_color="black")
nx.draw_networkx_nodes(G, pos, art_points, node_color="red")
