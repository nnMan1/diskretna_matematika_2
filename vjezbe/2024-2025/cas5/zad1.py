#https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=251

def dfs_articulation_points(G):

    n = len(G)  # Number of nodes

    visited = [False] * (n + 1)
    tin = [-1] * (n + 1)
    tmin = [-1] * (n + 1)

    timer = [0]
    articulation_points_set = []

    def dfs(u, parent):
        visited[u] = True
        tin[u] = timer[0]
        tmin[u] = timer[0]
        timer[0] += 1

        children_count = 0  
        is_articulation = False  

        for v in G[u]:
            if v == parent:
                continue

            if not visited[v]:
                children_count += 1
                dfs(v, u)
                tmin[u] = min(tmin[u], tmin[v])
                if parent != -1 and tmin[v] >= tin[u]:
                    is_articulation = True
            else:
                tmin[u] = min(tmin[u], tin[v])

        if parent == -1 and children_count > 1:
            is_articulation = True

        if is_articulation:
            articulation_points_set.append(u)

    for node in G:
        if not visited[node]:
            dfs(node, -1)

    return articulation_points_set




while True:
  n = int(input())

  if n == 0:
    break

  nodes = {i: [] for i in range(1, n+1)}

  while True:
    line = input()
    line = line.strip()

    if line == '0':
      break

    nums = line.split(' ')
    nums = [int(n) for n in nums]
    
    for u in nums[1:]:
      nodes[u].append(nums[0])
      nodes[nums[0]].append(u)

  print(len(dfs_articulation_points(nodes)))

