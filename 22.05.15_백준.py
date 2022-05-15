#다시 BFS/DFS 마스터하자(해본적은 있던가?)
#14502 연구소
import sys
import copy
from collections import deque
input = sys.stdin.readline

def bfs():
    global max_res
    graph_backup = [[0]*m for _ in range(n)]
    q = deque()
    res = 0
    for i in range(n):
        for j in range(m):
            graph_backup[i][j] = graph[i][j]
            if graph_backup[i][j] == 2:
                q.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph_backup[nx][ny] == 0:
                    graph_backup[nx][ny] = 2
                    q.append([nx, ny])
    for i in graph_backup:
        for j in i:
            if j == 0:
                res += 1
    max_res = max(max_res, res)

def dfs():
    global max_res
    graph_backup = [[0]*m for _ in range(n)]
    stack = deque()
    res = 0
    for i in range(n):
        for j in range(m):
            graph_backup[i][j] = graph[i][j]
            if graph_backup[i][j] == 2:
                stack.append([i, j])
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph_backup[nx][ny] == 0:
                    graph_backup[nx][ny] = 2
                    stack.append([nx, ny])
    for i in graph_backup:
        for j in i:
            if j == 0:
                res += 1
    max_res = max(max_res, res)



def wall(cnt):
    if cnt == 3:
        # bfs()
        dfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt+1) #재귀함수로 우선 벽을 세우기
                graph[i][j] = 0

# def dfs(graph, x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m:
#             if graph[nx][ny] == 0:
#                 graph[nx][ny] = 2
#                 print(np.array(graph))
#                 dfs(graph, nx, ny)
#
# def dfs_wall(cnt):
#     global max_res
#     if cnt == 3:
#         graph_backup = copy.deepcopy(graph)
#         res = 0
#         for i in range(n):
#             for j in range(m):
#                 if graph_backup[i][j] == 2:
#                     dfs(graph_backup, i, j)
#         for i in range(n):
#             for j in range(m):
#                 if graph_backup[i][j] == 2:
#                     res += 1
#         max_res = max(max_res, res)
#     else:
#         for i in range(n):
#             for j in range(m):
#                 if graph[i][j] == 0:
#                     graph[i][j] = 1
#                     dfs_wall(cnt+1)
#                     graph[i][j] = 0

max_res = 0
n , m = map(int, input().split())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    graph.append(list(map(int, input().split())))
# bfs_wall(0)
wall(0)
print(max_res)

