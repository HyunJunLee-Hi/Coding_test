#20056 마법사 상어와 파이어볼
#다시 풀어보기
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
fireball = []

for i in range(m):
    r, c, m, s, d = map(int, input().split())
    fireball.append([r-1, c-1])
    graph[r-1][c-1].append([m, s, d])

for _ in range(k):
    for j in range(len(fireball)):
        x, y = fireball.pop(0)
        m, s, d = graph[x][y].pop(0)
        nx = (x+(dx[d]*s))%n
        ny = (y+(dy[d]*s))%n
        graph[nx][ny].append([m, s, d])
    # print(graph)
    # print(fireball)
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) > 1:
                temp_m, temp_s, temp_even, temp_odd, cnt = 0, 0, 0, 0, 0
                while graph[i][j]:
                    m, s, d = graph[i][j].pop(0)
                    temp_m += m
                    temp_s += s
                    cnt += 1
                    if d%2 == 0:
                        temp_even += 1
                    else:
                        temp_odd += 1
                temp_m = temp_m//5
                if temp_m == 0:
                    continue
                temp_s = temp_s//cnt
                if temp_even == cnt or temp_odd == cnt:
                    direct = [0, 2, 4, 6]
                else:
                    direct = [1, 3, 5, 7]
                for d in range(4):
                    fireball.append([i, j])
                    graph[i][j].append([temp_m, temp_s, direct[d]])
            elif len(graph[i][j]) == 1:
                fireball.append([i, j])
    # print(graph)
    # print(fireball)

answer = 0
for i in range(n):
    for j in range(n):
        answer += sum(lst[0] for lst in graph[i][j])
print(answer)

# import sys
# from collections import deque
# import numpy as np
# import copy
# input = sys.stdin.readline
#
# def direction_check(visited):
#     #0 모두 짝수 or 홀수 방향, 1 그 외
#     even = 0
#     odd = 0
#     for i in range(len(visited)):
#         d = visited[i][2]
#         if d%2 == 0:
#             even += 1
#         else:
#             odd += 1
#     if (even and not odd) or (odd and not even):
#         return 1
#     else:
#         return 0
#
#
# def move_and_divide(graph, fireball):
#     while fireball:
#         r, c, m, s, d = fireball.pop(0)
#         graph[(r+(dx[d]*s))%N][(c+(dy[d]*s))%N].append([m, s, d])
#     # print(graph)
#     for i in range(N):
#         for j in range(N):
#             if len(graph[i][j]) >= 2:
#                 temp_m, temp_s, temp_d, cnt = 0, 0, 0, len(graph[i][j])
#                 chk = direction_check(graph[i][j])
#                 if chk == 1:
#                     while graph[i][j]:
#                         temp = graph[i][j].pop(0)
#                         temp_m += temp[0]
#                         temp_s += temp[1]
#                         temp_d += temp[2]
#                     if temp_m // 5 == 0:
#                         continue
#                     for d in range(0, 8, 2):
#                         graph[i][j].append([temp_m//5, temp_s//cnt, d])
#                 else:
#                     temp_m, temp_s, temp_d = 0, 0, 0
#                     while graph[i][j]:
#                         temp = graph[i][j].pop()
#                         temp_m += temp[0]
#                         temp_s += temp[1]
#                         temp_d += temp[2]
#                     if temp_m // 5 == 0:
#                         continue
#                     for d in range(1, 8, 2):
#                         graph[i][j].append([temp_m // 5, temp_s // cnt, d])
#                 # temp_graph = [[[] for _ in range(N)] for _ in range(N)]
#                 # for i in range(N):
#                 #     for j in range(N):
#                 #         # print(graph[i][j])
#                 #         while graph[i][j]:
#                 #             m, s, d = graph[i][j].pop(0)
#                 #             # print(m, s, d)
#                 #             temp_graph[(i + (dx[d] * s)) % N][(j + (dy[d] * s)) % N].append([m, s, d])
#                 # graph = temp_graph
#     for i in range(N):
#         for j in range(N):
#             if len(graph[i][j]) == 1:
#                 # print(graph[i][j])
#                 fireball.append([i, j, graph[i][j][0][0], graph[i][j][0][1], graph[i][j][0][2]])
#
#     # for i in range(N):
#     #     for j in range(N):
#     #         if len(temp_graph[i][j]) == 1:
#     #             fireball.append([i, j, temp_graph[i][j][0][0], temp_graph[i][j][0][1], temp_graph[i][j][0][2]])
#     print(graph)
#     print(fireball)
#     return graph, fireball
#
#
#
# N, M, K = map(int, input().split())
# graph = [[[] for _ in range(N)] for _ in range(N)]
# fireball = []
# dx = [-1, -1, 0, 1, 1, 1, 0, -1]
# dy = [0, 1, 1, 1, 0, -1, -1, -1]
# for i in range(M):
#     r, c, m, s, d = map(int, input().split())
#     fireball.append([r - 1, c - 1, m, s, d])
# for k in range(K):
#     graph, fireball = move_and_divide(graph, fireball)
# answer = 0
# for i in range(N):
#     for j in range(N):
#         for k in range(len(graph[i][j])):
#             answer += graph[i][j][k][0]
# print(answer)