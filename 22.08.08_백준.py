#2468 안전 영역
import sys
from collections import deque
import copy
# import numpy as np
input = sys.stdin.readline

def bfs(graph, visited, n, start, height):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > height:
                    if visited[nx][ny] == 0:
                        q.append([nx, ny])
                        visited[nx][ny] = 1
                        # print(np.array(visited))
    return visited

n = int(input())
graph = []
max_height = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[0]*n for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in temp:
        if max_height < j:
            max_height = j
    graph.append(temp)

max_cnt = 0
for h in range(max_height+1):
    cnt = 0
    visited_temp = copy.deepcopy(visited)
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and visited_temp[i][j] == 0:
                visited_temp = bfs(graph, visited_temp, n, [i, j], h)
                cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
