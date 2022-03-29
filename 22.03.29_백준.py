#2225 합분해
#DP
# import sys
# from itertools import permutations
#
# input = sys.stdin.readline
# n, k = map(int, input().split())
# lst = []
# for i in range(n+1):
#     for j in range(k//2+1):
#         lst.append(i)
# res = list(set(permutations(lst, k)))
#
# answer = 0
# for target in res:
#     if sum(target) == n:
#         answer += 1
# print(answer%1000000000)

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
graph = [([0]*201) for _ in range(201)]
for i in range(201):
    graph[i][1] = i
    graph[1][i] = 1
for i in range(2, 201):
    for j in range(2, 201):
        temp = graph[i][j-1] + graph[i-1][j]
        graph[i][j] = temp
print(graph[k][n]%1000000000)
