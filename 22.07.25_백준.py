#2096 내려가기
#다시 풀기
import copy
import sys
input = sys.stdin.readline

n = int(input())
dp_Max = [0]*3
dp_min = [0]*3
temp_Max = [0]*3
temp_min = [0]*3
# graph = []

# for i in range(n):
#     graph.append(list(map(int, input().split())))

# dp_Max[0] = copy.deepcopy(graph[0])
# dp_min[0] = copy.deepcopy(graph[0])
for i in range(n):
    x, y, z = map(int, input().split())
    # if i == 0:
    #     dp_Max = [x, y, z]
    #     dp_min = [x, y, z]
    # else:
    for j in range(3):
        if j == 0:
            temp_Max[j] = x + max(dp_Max[0], dp_Max[1])
            temp_min[j] = x + min(dp_min[0], dp_min[1])
        elif j == 1:
            temp_Max[j] = y + max(dp_Max[0], dp_Max[1], dp_Max[2])
            temp_min[j] = y + min(dp_min[0], dp_min[1], dp_min[2])
        elif j == 2:
            temp_Max[j] = z + max(dp_Max[1], dp_Max[2])
            temp_min[j] = z + min(dp_min[1], dp_min[2])
    for j in range(3):
        dp_Max[j] = temp_Max[j]
        dp_min[j] = temp_min[j]
    # print(dp_Max, dp_min)
# print(max(dp_Max[-1]), min(dp_min[-1]))
print(max(dp_Max), min(dp_min))