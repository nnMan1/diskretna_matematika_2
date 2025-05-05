def dfs_find_bridges(G):

  timer = 0
  visited = {u: False for u in G}
  tin = {u: -1 for u in G}
  tree_edges = []
  bridges = []
  back_edges = []

  back_edges_start = {u: 0 for u in G}
  back_edges_end = {u: 0 for u in G}

  def dfs(source, parent):
    nonlocal timer

    if visited[source]:
      if parent != -1 and tin[source] < tin[parent]:
        back_edges_end[source] += 1
        back_edges_start[parent] += 1
        back_edges.append((parent, source))
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

  for u in G:
    if visited[u] == False:
      dfs(u, -1)

  return bridges, tree_edges, back_edges

i = 1
while True:
    line = input()
    n, m = line.split(" ")
    n, m = int(n), int(m)

    if n == 0 and m == 0:
      break

    nodes = {i: [] for i in range(1, n+1)}

    for _ in range(m):
      line = input()
      x, y = line.split(" ")
      x, y = int(x), int(y)

      nodes[x].append(y)
      nodes[y].append(x)

    bridges, tree_edges, back_edges = dfs_find_bridges(nodes)

    print(i)
    print()

    for u,v in bridges:
      print(u, v) #drugi put ce da se stampaju ka tree edges

    for u,v in tree_edges:
      print(u, v)

    for u, v in back_edges:
      print(v, u)

    print("#")
