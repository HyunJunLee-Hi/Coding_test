# #12865 평범한 배낭
# import sys
#
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
# dp = [[0]*(k+1) for _ in range(n+1)]
#
#
# for i in range(n):
#     w, v = map(int, input().split())
#     for j in range(n):
#         if i == 0:
#             dp[0] = [w, v]
#         else:
#             if dp[i-1][0] + w <= k:
#                 dp[i][0] = dp[i-1][0] + w
#                 dp[i][1] = dp[i-1][1] + v
#             else:
#                 dp[i] = [w, v]
#
# dp.sort(key=lambda x : x[1], reverse = True)
#
# print(dp[0][1])

#12865 평범한 배낭
#어렵다...
#다시 풀기
import sys
# import numpy as np
input = sys.stdin.readline

n, k = map(int, input().split())
d = [[0]*(k+1) for _ in range(n+1)]
w = []
v = []

for i in range(n):
    x, y = map(int, input().split())
    w.append(x)
    v.append(y)

for i in range(1, n+1):
    for j in range(1, k+1):
        if j < w[i-1]:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w[i-1]] + v[i-1])
        # temp = np.array(d)
        # print(w)
        # print(v)
        # print(temp)
print(max(d[n]))


#14503 로봇 청소기
#틀린 정답
import sys
from collections import deque
import numpy as np
input = sys.stdin.readline

def clean(graph, start, d, cnt):
    x, y = start
    if graph[x][y] == 0:
        graph[x][y] = 2
        cnt += 1
    flag = 0
    temp = 0
    for i in range(4):
        temp += 1
        d = (d-1)%4
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx <= n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                print(np.array(graph))
                cnt += 1
                flag = 1
                cnt = clean(graph, [nx, ny], d, cnt)
    if flag == 1:
        if temp == 3:
            if graph[nx-dx[d]][ny-dy[d]] == 1:
                return cnt
        else:
            cnt = clean(graph, [nx-dx[d], ny-dy[d]], d, cnt)

    return cnt



n, m = map(int, input().split())
r, c, d = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
print(clean(graph, [r, c], d, 0))

