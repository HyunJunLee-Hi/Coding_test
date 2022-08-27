# #14499 주사위 굴리기
import sys
input = sys.stdin.readline

def dice_change(d, dice):
    if d == 0:
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif d == 1:
        dice[0], dice[3], dice[5], dice[2] = dice[2], dice[0], dice[3], dice[5]
    elif d == 2:
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]
    elif d == 3:
        dice[0], dice[4], dice[5], dice[1] = dice[1], dice[0], dice[4], dice[5]

n, m, x, y, k = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
move = list(map(int, input().split()))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]
for d in move:
    nx = x + dx[d-1]
    ny = y + dy[d-1]
    if 0 <= nx < n and 0 <= ny < m:
        dice_change(d-1, dice)
        if graph[nx][ny] != 0:
            dice[5] = graph[nx][ny]
            graph[nx][ny] = 0
        else:
            graph[nx][ny] = dice[5]
        x, y = nx, ny
        print(dice[0])
#
#
#

#15686 치킨 배달
# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# graph = []
# chicken = []
# house = []
# for i in range(n):
#     temp = list(map(int, input().split()))
#     for j in range(n):
#         if temp[j] == 0:
#             continue
#         elif temp[j] == 1:
#             house.append([i, j, 0])
#         elif temp[j] == 2:
#             chicken.append([i, j, 0])
#     graph.append(temp)
# for i in range(len(house)):
#     x, y, c_len = house[i]
#     temp = []
#     for j in range(len(chicken)):
#         temp.append(abs(x-chicken[j][0]) + abs(y-chicken[j][1]))
#     c_len = min(temp)
#     target_chicken = temp.index(c_len)
#     chicken[target_chicken][2] += 1
#     house[i] = [x, y, c_len]
# chicken.sort(reverse = True, key = lambda x : x[2])
# for i in range(len(chicken)):
#     if i >= m:
#         graph[chicken[i][0]][chicken[i][1]] = 0
# print(graph)
# for i in range(len(house)):
#     house[i][2] = 0
# new_chicken = []
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 2:
#             new_chicken.append([i, j])
# for i in range(len(house)):
#     x, y, c_len = house[i]
#     temp = []
#     for j in range(len(new_chicken)):
#         temp.append(abs(x-new_chicken[j][0]) + abs(y-new_chicken[j][1]))
#     c_len = min(temp)
#     target_chicken = temp.index(c_len)
#     house[i] = [x, y, c_len]
# answer = 0
# for h in house:
#     answer += h[2]
# print(answer)

import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
chicken = []
house = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 0:
            continue
        elif temp[j] == 1:
            house.append([i, j])
        elif temp[j] == 2:
            chicken.append([i, j])
    graph.append(temp)
answer = 999999
target = list(combinations(chicken, m))
for chick in target:
    res = 0
    for h in house:
        c_len = 999
        for j in range(m):
            c_len = min(c_len, abs(h[0]-chick[j][0]) + abs(h[1]-chick[j][1]))
        res += c_len
    answer = min(answer, res)
print(answer)