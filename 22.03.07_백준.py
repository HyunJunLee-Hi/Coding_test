#1926 그림
import sys
from collections import deque

def bfs(i, j, graph):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    xy = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    xy += 1
                    q.append((nx, ny))
    return xy
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, sys.stdin.readline().split())

graph = []
visited = [[0]*m for _ in range(n)]
cnt = 0
res = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            tmp = bfs(i, j, graph)
            res.append(tmp)
if cnt == 0:
    print(0)
    print(0)
else:
    print(cnt)
    print(max(res))


