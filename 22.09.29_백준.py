#21608 상어 초등학교
import sys
input = sys.stdin.readline

n = int(input())
graph = [[0]*n for _ in range(n)]
informations = [list(map(int, input().split())) for _ in range(n**2)]
dx = [-1, 0 ,1, 0]
dy = [0, 1, 0, -1]
for l in range(n**2):
    student = informations[l]
    temp = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                blank = 0
                friend = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] in student[1:]:
                            friend += 1
                        if graph[nx][ny] == 0:
                            blank += 1
                temp.append([friend, blank, i, j])
    temp.sort(key=lambda x : (-x[0], -x[1], x[2], x[3]))
    graph[temp[0][2]][temp[0][3]] = student[0]
# print(graph)
informations.sort()
res = 0

for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] in informations[graph[i][j]-1][1:]:
                    cnt += 1
        if cnt != 0:
            res += 10**(cnt-1)
print(res)

