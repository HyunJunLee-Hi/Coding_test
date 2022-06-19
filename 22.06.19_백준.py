#2583 영역 구하기
#다시 풀어보기
import sys
# from collections import deque
# # import numpy as np
input = sys.stdin.readline
#
# def bfs(start, cnt, res):
#     cnt += 1
#     q = deque()
#     q.append(start)
#     visited[start[0]][start[1]] = 1
#     size = 1
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < m and 0 <= ny < n:
#                 if graph[nx][ny] == 0 and visited[nx][ny] == 0:
#                     visited[nx][ny] = 1
#                     size += 1
#                     q.append([nx, ny])
#     # print(np.array(visited))
#     res.append(size)
#     return cnt, visited
# m, n, k = map(int, input().split())
# square = []
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# cnt = 0
# res = []
# visited = [[0]*n for _ in range(m)]
# for i in range(k):
#     square.append(list(map(int, input().split())))
# graph = [[0]*n for _ in range(m)]
# for s in square:
#     for i in range(s[0], s[2]):
#         for j in range(s[1], s[3]):
#             graph[j][i] = 1
# for i in range(m):
#     for j in range(i):
#         if graph[i][j] == 0 and visited[i][j] == 0:
#             cnt, visited = bfs([i, j], cnt, res)
#
# print(cnt)
# res.sort()
# print(res)

m, n, k = map(int, input().split())
graph = [[0]*n for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = []
for i in range(k):
    square = list(map(int, input().split()))
    for j in range(square[1], square[3]):
        for l in range(square[0], square[2]):
            graph[j][l] = 1
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            count = 1
            graph[i][j] = 1
            q = [[i, j]]
            while q:
                x, y = q.pop(0)
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < m and 0 <= ny < n:
                        if graph[nx][ny] == 0:
                            graph[nx][ny] = 1
                            count += 1
                            q.append([nx, ny])
            cnt.append(count)
print(len(cnt))
cnt.sort()
for i in cnt:
    print(i, end=' ')