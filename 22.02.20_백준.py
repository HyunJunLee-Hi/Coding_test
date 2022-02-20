#11724 연결 요소의 개수
import sys
from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        i = q.popleft()
        for j in range(n):
            if graph[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                q.append(j)

def dfs(v):
    stack = []
    stack.append(v)
    visited[v] = 1
    while stack:
        i = stack.pop()
        for j in range(n):
            if graph[i][j] == 1 and i != j and visited[j] == 0:
                visited[j] = 1
                stack.append(j)

n, m = map(int, sys.stdin.readline().split())
graph = [[0]*n for _ in range(n)]
visited = [0]*n
res = 0

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    x -= 1
    y -= 1
    graph[x][y] = 1
    graph[y][x] = 1

for i in range(n):
    if visited[i] == 0:
        #bfs(i)
        dfs(i)
        res += 1

print(res)


#4963 섬의 개수
#visted 쓰면 안되는 이유가 뭘까?
import sys
from collections import deque

def bfs(graph, i, j):
    # q = deque()
    # q.append([i, j])
    graph[i][j] = 0
    q = [[i, j]]
    #visited[i][j] = 1
    while q:
        tmp = q.pop(0)
        # print(tmp)
        x, y = tmp[0], tmp[1]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1:
                    #if visited[nx][ny] == 0:
                    graph[nx][ny] = 0
                    q.append([nx, ny])

dx = [1, -1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]
while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    graph = []
    #visited = [[0]*w for i in range(h)]
    cnt = 0
    for i in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                # import numpy as np
                # print(np.array(visited))
                cnt += 1
    print(cnt)


#6603 로또
#DFS로도 풀 수 있다니...
import sys
from itertools import combinations

while True:
    case = list(map(int, sys.stdin.readline().split()))
    if case[0] == 0:
        break
    n = case.pop(0)
    lst = list(combinations(case, 6))
    for i in lst:
        for j in i:
            print(j, end=' ')
        print()
    print()

import sys

def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end =' ')
        print()
        return
    for i in range(start, n):
        combi[depth] = case[i]
        dfs(i+1, depth+1)

while True:
    case = list(map(int, sys.stdin.readline().split()))
    if case[0] == 0:
        break
    n = case.pop(0)
    combi = [0]*n
    dfs(0, 0)
    print()









