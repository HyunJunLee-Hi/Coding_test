#17143 낚시왕
import sys
input = sys.stdin.readline

def move(graph):
    temp_graph = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] != []:
                s, d, z = graph[i][j][0]
                graph[i][j] = []
                x, y, temp = i, j, s
                while s:
                    x += dx[d]
                    y += dy[d]
                    if 0 <= x < R and 0 <= y < C:
                        s -= 1
                    else:
                        x -= dx[d]
                        y -= dy[d]
                        if d == 0:
                            d = 1
                        elif d == 1:
                            d = 0
                        elif d == 2:
                            d = 3
                        elif d == 3:
                            d = 2
                if temp_graph[x][y] == []:
                    temp_graph[x][y].append([temp, d, z])
                else:
                    if temp_graph[x][y][0][2] < z:
                        temp_graph[x][y] = []
                        temp_graph[x][y].append([temp, d, z])

    return temp_graph

R, C, M = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
graph = [[[] for _ in range(C)] for _ in range(R)]
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    graph[r-1][c-1].append([s, d-1, z])
answer = 0
for i in range(C):
    for j in range(R):
        if graph[j][i] != []:
            answer += graph[j][i][0][2]
            graph[j][i] = []
            break
    graph = move(graph)
print(answer)
