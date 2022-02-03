import sys
from collections import deque

def dfs(a):
    print(a, end = ' ')
    visited[a] = True
    for i in graph[a]:
        if not visited[i]:
            dfs(i)

def bfs(a):
    visited[a] = True
    q = deque([a])
    while q:
        b = q.popleft()
        print(b, end = ' ')
        for i in graph[b]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    
    
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    node, nex = map(int, sys.stdin.readline().split())
    graph[node].append(nex)
    graph[nex].append(node)

for i in range(1, n + 1):
    graph[i].sort()
    
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)