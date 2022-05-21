#14503 로봇 청소기
#아직도 어려워...
#이해가 안가..
# import sys
# from collections import deque
# import numpy as np
# input = sys.stdin.readline
#
# def dfs(graph, visited, n, m, start, d):
#     q = deque()
#     q.append(start)
#     visited[start[0]][start[1]] = 1
#     graph[start[0]][start[1]] = 2
#     res = 1
#     while q:
#         x, y = q.popleft()
#         cnt = 0
#         for i in range(4):
#             d = (d - 1) % 4
#             nx = x + dx[d]
#             ny = y + dy[d]
#             if cnt == 4:
#                 back_x = x + dx[(d-2)%4]
#                 back_y = y + dy[(d-2)%4]
#                 # if 0 <= back_x < n and 0 <= back_y < m and graph[back_x][back_y] == 0 and visited[back_x][back_y] == 0:
#                 #     q.apppend([back_x, back_y])
#                 #     continue
#                 # else:
#                 #     return res
#                 if graph[back_x][back_y] == 1:
#                     return res
#                 else:
#                     q.apppend([back_x, back_y])
#             if 0 <= nx < n and 0 <= ny < m:
#                 if graph[nx][ny] == 0 and visited[nx][ny] == 0:
#                     q.append([nx, ny])
#                     graph[nx][ny] = 2
#                     visited[nx][ny] = 1
#                     res += 1
#                     # d = (d - 1) % 4
#                     print(np.array(graph))
#                     print(res)
#                 else:
#                     cnt += 1
#                     d = (d-1)%4
#     return res
#
# n, m = map(int, input().split())
# r, c, d = map(int, input().split())
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# visited = [[0]*m for _ in range(n)]
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))
# res = dfs(graph, visited, n, m, [r, c], d)
# print(res)
#
#

import sys
from collections import deque
# import numpy as np
input = sys.stdin.readline
#
# n, m = map(int, input().split())
# r, c, d = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# def bfs(x, y, d):
#     res = 0
#     q = deque()
#
#     q.append((x,y,d))
#     graph[x][y] = 2
#     res += 1
#
#     while q:
#         x, y, d = q.popleft()
#         temp_d = d
#         cnt = 0
#         for i in range(4):
#             print((temp_d+3)%4)
#             nx = x + dx[(temp_d+3)%4]
#             ny = y + dy[(temp_d+3)%4]
#             temp_d = (temp_d+3)%4
#             if 0 <= nx < n and 0 <= ny < m:
#                 if graph[nx][ny] == 0:
#                     q.append((nx, ny, (temp_d+3)%4))
#                     graph[nx][ny] = 2
#                     res += 1
#                     print(np.array(graph))
#                     print(res)
#                     break
#                 else:
#                     cnt += 1
#         if cnt == 4:
#             back_x = x + dx[(d-2)%4]
#             back_y = y + dy[(d-2)%4]
#             if graph[back_x][back_y] == 1:
#                 return res
#
#             q.append((back_x, back_y, d))
#
# print(bfs(r, c, d))


n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, d):
    res = 0
    q = deque()

    q.append((x, y, d))
    graph[x][y] = 2
    res += 1

    while q:
        x, y, d = q.popleft()
        temp_d = d
        cnt = 0
        for i in range(4):
            nd = (temp_d+3)%4
            nx = x + dx[nd]
            ny = y + dy[nd]
            temp_d = nd

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    q.append((nx, ny, nd))
                    graph[nx][ny] = 2
                    res += 1
                    # print(np.array(graph))
                    # print(res)
                    break
                else:
                    cnt += 1
        if cnt == 4:
            bx = x + dx[(d+2)%4]
            by = y + dy[(d+2)%4]
            if graph[bx][by] == 1:
                return res
            q.append((bx, by, d))

print(bfs(r, c, d))
