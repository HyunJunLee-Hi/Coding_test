#21609 상어 중학교
#다시 풀어보기
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, color):
    q = deque()
    q.append([x, y])

    block_cnt, rainbow_cnt = 1, 0
    blocks, rainbows = [[x, y]], []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and graph[nx][ny] == color:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    block_cnt += 1
                    blocks.append([nx, ny])
                elif visited[nx][ny] == 0 and graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    block_cnt += 1
                    rainbow_cnt += 1
                    rainbows.append([nx, ny])
    for x, y in rainbows:
        visited[x][y] = 0

    return [block_cnt, rainbow_cnt, blocks+rainbows]

def gravity(graph):
    for i in range(n-1, -1 ,-1):
        for j in range(n):
            if graph[i][j] > -1:
                r = i
                while True:
                    if 0 <= r+1 < n and graph[r+1][j] == -2:
                        graph[r+1][j] = graph[r][j]
                        graph[r][j] = -2
                        r += 1
                    else:
                        break

def rotation(graph):
    temp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[n-1-j][i] = graph[i][j]
    return temp

n, m = map(int, input().split())
graph = []
answer = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    graph.append(list(map(int, input().split())))

while True:
    visited = [[0]*n for _ in range(n)]
    blocks = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0 and visited[i][j] == 0:
                visited[i][j] = 1
                block_info = bfs(i, j, graph[i][j])
                if block_info[0] >= 2:
                    blocks.append(block_info)
    blocks.sort(reverse=True)
    # print(blocks)

    if not blocks:
        break

    for x, y in blocks[0][2]:
        graph[x][y] = -2
    answer += blocks[0][0]**2

    gravity(graph)

    graph = rotation(graph)

    gravity(graph)

print(answer)

# def bfs(graph, color_lst, color, start):
#     q = deque()
#     q.append(start)
#     visited[start[0]][start[1]] = 1
#     cnt = 1
#     block = [start[0], start[1]]
#     while q:
#         x, y = q.pop()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if graph[nx][ny] != -1:
#                     if graph[nx][ny] == color and visited[nx][ny] == 0:
#                         visited[nx][ny] = 1
#                         cnt += 1
#                         q.append([nx, ny])
#                         if nx < x:
#                             block[0], block[1] = nx, ny
#                         elif ny < y:
#                             block[0], block[1] = nx, ny
#                     elif graph[nx][ny] == 0 and visited[nx][ny] != 2:
#                         visited[nx][ny] = 2
#                         cnt += 1
#                         q.append([nx, ny])
#
#     try:
#         if color_lst[color][0] < cnt:
#             color_lst[color].pop()
#             color_lst[color].append([cnt, x, y])
#     except:
#         color_lst[color].append([cnt, block[0], block[1]])
#     for i in range(m+1):
#         color_lst[i].sort(key = lambda x : (-x[0], x[1], x[2]))
#     print(color_lst)
#     return color_lst
#
# n, m = map(int, input().split())
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# graph = []
# color_lst = [[] for _ in range(m+1)]
# visited = [[0] * n for _ in range(n)]
# for i in range(n):
#     graph.append(list(map(int, map(int, input().split()))))
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] != 0 and graph[i][j] != -1 and visited[i][j] != 1:
#             color_lst = bfs(graph, color_lst, graph[i][j], [i, j])
