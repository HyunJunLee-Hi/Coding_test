#21609 상어 중학교
import sys
from collections import deque
import numpy as np
input = sys.stdin.readline

def bfs(graph, visited, color, start):
    blocks = [start]
    rainbows = []
    block_cnt = 1
    rainbow_cnt = 0
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = 1
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
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
while True:
    target = []
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                target.append(bfs(graph, visited, graph[i][j], [i, j]))
    target.sort(reverse=True)
    if target[0][0] >= 2:
        for x, y in target[0][2]:
            graph[x][y] = -2
        answer += target[0][0]**2

    else:
        break

    gravity(graph)
    graph = rotation(graph)
    gravity(graph)

print(answer)