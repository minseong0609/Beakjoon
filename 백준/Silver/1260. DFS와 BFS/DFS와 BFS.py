from collections import deque

def dfs (graph, root):
    visited = []
    dfs_que = deque([root])
    while dfs_que:
        n = dfs_que.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:

                temp = list( set(graph[n])-set(visited) )
                temp.sort(reverse=True)
                dfs_que += temp

    return " ".join(str(i) for i in visited)

def bfs (graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visited)



n, m, v = map(int, input().split())
graph = {}
for i in range(m):
    n1, n2 = map(int, input().split(' '))

    if ( n1 not in graph ):
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if ( n2 not in graph ):
        graph[n2] = [n1]
    elif (n1 not in graph[n2]):
        graph[n2].append(n1)

print(dfs(graph, v))
print(bfs(graph, v))
