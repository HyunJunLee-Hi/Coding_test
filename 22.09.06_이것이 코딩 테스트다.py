import sys
input = sys.stdin.readline
#상하좌우
n = int(input())
graph = [[0]*n for _ in range(n)]
move = {}
move['R'] = [0, 1]
move['L'] = [0, -1]
move['U'] = [-1, 0]
move['D'] = [1, 0]

motion = list(input().split())
start = [0, 0]
for i in motion:
    if 0 <= start[0]+move[i][0] < n and 0 <= start[1]+move[i][1] < n:
        start[0] += move[i][0]
        start[1] += move[i][1]
    else:
        continue
print(start[0]+1, start[1]+1)


#시각
cnt = 0
hour = int(input())
for h in range(hour+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                cnt += 1
print(cnt)


#왕실의 나이트
move = [[-1, -2], [1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, -1], [2, 1]]
column = {}
column['a'] = 1
column['b'] = 2
column['c'] = 3
column['d'] = 4
column['e'] = 5
column['f'] = 6
column['g'] = 7
column['h'] = 8

location = input()
c = column[location[0]]-1
r = int(location[1])-1
graph = [[0]*8 for _ in range(8)]
cnt = 0
for i in range(8):
    if 0 <= r+move[i][0] < 8 and 0 <= c+move[i][1] < 8:
        cnt += 1
print(cnt)


#게임 개발
#잉?
import numpy as np
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# n, m = map(int, input().split())
# x, y, d = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))
# answer = 1
# q = [[x, y, d]]
# graph[x][y] = 2
# while q:
#     x, y, d = q.pop(0)
#     d -= 1
#     nx = x + dx[d]
#     ny = y + dy[d]
#     print(nx, ny)
#     if 0 <= nx < n and 0 <= ny < m:
#         if graph[nx][ny] == 0:
#             answer += 1
#             graph[nx][ny] = 2
#             q.append([nx, ny, d])
#         elif graph[nx][ny] == 2:
#             continue
#         elif d < -4 and (graph[nx][ny] == 1 or graph[nx][ny] == 2):
#             if graph[nx-dx[d]][ny-dy[d]] == 1:
#                 break
#             else:
#                 d = 0
#                 q.append([nx-dx[d], ny-dy[d], d])
#     else:
#         print(23233)
# print(answer)