#15686 치킨 배달
import sys
# from collections import deque
from itertools import combinations
# from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
chicken = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 2:
            chicken.append([i, j])
    graph.append(temp)
target_lst = list(combinations(chicken, m))
# target_lst_ = list(permutations(chicken, m))
res = sys.maxsize
for target in target_lst:
    res_temp = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                temp = sys.maxsize
                for l in range(m):
                    temp = min(temp, abs(target[l][0]-i)+abs(target[l][1]-j))
                res_temp += temp
    res = min(res, res_temp)
print(res)


