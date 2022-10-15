#17144 미세먼지 안녕!
import copy
import sys
input = sys.stdin.readline

def spread(graph, machine):
    temp = [[0]*c for _ in range(r)]
    for i, j in machine:
        temp[i][j] = -1
    # temp = copy.deepcopy(graph)
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                cnt = 0
                sp = graph[i][j]//5
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                        cnt += 1
                        temp[nx][ny] += sp
                temp[i][j] += graph[i][j] - (sp * cnt)
    graph = temp

    return graph

def work(graph, machine):
    temp = copy.deepcopy(graph)
    x1, y1 = machine[0]
    x2, y2 = machine[1]
    for i in range(2, c):
        graph[x1][i] = temp[x1][i-1]
    for i in range(x1-1, -1, -1):
        graph[i][c-1] = temp[i+1][c-1]
    for i in range(c-2, -1, -1):
        graph[0][i] = temp[0][i+1]
    for i in range(1, x1):
        graph[i][0] = temp[i-1][0]
    graph[x1][1] = 0

    for i in range(2, c):
        graph[x2][i] = temp[x2][i - 1]
    for i in range(x2 + 1, r):
        graph[i][c - 1] = temp[i - 1][c - 1]
    for i in range(c - 2, -1, -1):
        graph[r-1][i] = temp[r-1][i + 1]
    for i in range(r-2, x2, -1):
        graph[i][0] = temp[i + 1][0]
    graph[x2][1] = 0

    return graph

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
r, c, t = map(int, input().split())
machine = []
graph = []
for i in range(r):
    temp = list(map(int, input().split()))
    for j in range(c):
        if temp[j] == -1:
            machine.append([i, j])
    graph.append(temp)
x1, y1 = machine[0]
x2, y2 = machine[1]
for _ in range(t):
    graph = spread(graph, machine)
    graph = work(graph, machine)
answer = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            answer += graph[i][j]
print(answer)
