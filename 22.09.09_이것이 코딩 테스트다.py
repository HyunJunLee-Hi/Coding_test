#게임 개발
import numpy as np
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
answer = 1
graph[x][y] = 2
turn_cnt = 0
while True:
    #왼쪽으로 회정
    d = (d-1)%4
    turn_cnt += 1
    # 만약 왼쪽에 갈 곳이 있다면 전진 / 없다면 되돌아감
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < m:
        if graph[nx][ny] == 0:
            graph[nx][ny] = 2
            x, y = nx, ny
            turn_cnt = 0
            answer += 1
            print(np.array(graph))
    else:
        continue

    if turn_cnt == 4:
        d = (d+1)%4
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 1:
            x, y = nx, ny
            turn_cnt = 0
        else:
            break
print(answer)


#음료수 얼려 먹기
import sys
input = sys.stdin.readline

def dfs(graph, start):
    stack = []
    stack.append(start)
    graph[start[0]][start[1]] = 2
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    stack.append([nx, ny])

n, m = map(int, input().split())
graph = []
dx = [-1, 0 ,1, 0]
dy = [0, 1, 0, -1]
answer = 0
for i in range(n):
    temp = input()
    temp = list(str(temp).rstrip())
    for j in range(m):
        temp[j] = int(temp[j])
    graph.append(temp)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(graph, [i, j])
            answer += 1
print(answer)


#미로 탈출
import sys
import numpy as np
from collections import deque
input = sys.stdin.readline

def bfs(graph, start):
    q = deque()
    q.append(start)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx, ny])

n, m = map(int, input().split())
graph = []
visited = [[0]*m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    temp = input()
    temp = list(str(temp).rstrip())
    for j in range(m):
        temp[j] = int(temp[j])
    graph.append(temp)
answer = bfs(graph, [0, 0])
print(graph[n-1][m-1])