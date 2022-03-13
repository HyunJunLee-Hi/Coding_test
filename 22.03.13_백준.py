# #14890 경사로
# import sys
#
# n, l = map(int, sys.stdin.readline().split())
# graph = []
# cnt = 0
# for i in range(n):
#     graph.append(list(map(int, sys.stdin.readline().split())))
#
# for i in range(n):
#     #flag = 0
#     j = 0
#     while(j < n):
#         try:
#             if abs(graph[i][j] - graph[i][j+1]) > 1:
#                 j = n
#             elif (graph[i][j] - graph[i][j+1]) == 1:
#                 flag = 0
#                 for k in range(1, l+1):
#                     if (graph[i][j] - graph[i][j+k]) != 1:
#                         flag = 1
#                 if flag == 0:
#                     j += l
#             elif (graph[i][j] - graph[i][j-1]) == -1:
#                 flag = 0
#                 for k in range(1, l+1):
#                     if (graph[i][j] - graph[i][j+k]) != -1:
#                         flag = 1
#                 if flag == 0:
#                     j += l
#             j += 1
#         except:
#             break
#         if j == n-1:
#             cnt += 1
# for j in range(n):
#     #flag = 0
#     i = 0
#     while(j < n):
#         try:
#             if abs(graph[i][j] - graph[i][j+1]) > 1:
#                 j = n
#             elif (graph[i][j] - graph[i][j+1]) == 1: #하강
#                 flag = 0
#                 for k in range(1, l+1):
#                     if (graph[i][j] - graph[i][j+k]) != 1:
#                         flag = 1
#                 if flag == 0:
#                     j += l
#             elif (graph[i][j] - graph[i][j-1]) == -1:#상승
#                 flag = 0
#                 for k in range(1, l+1):
#                     if (graph[i][j] - graph[i][j+k]) != -1:
#                         flag = 1
#                 if flag == 0:
#                     j += l
#             j += 1
#         except:
#             break
#         if j == n-1:
#             cnt += 1
# print(cnt)

#14890 경사로
import sys

def check(line):
    sw = [0 for i in range(n)]
    for i in range(n-1):
        if line[i] == line[i+1]:
            continue
        if abs(line[i] - line[i+1]) > 1:
            return False
        if line[i] > line[i+1]:
            tmp = line[i+1]
            for j in range(i+1, i+1+l):
                if 0 <= j < n:
                    if line[j] != tmp:
                        return False
                    if sw[j] == 1:
                        return False
                    sw[j] = 1
                else:
                    return False
        else:
            tmp = line[i]
            for j in range(i, i-l, -1):
                if 0 <= j < n:
                    if line[j] != tmp:
                        return False
                    if sw[j] == 1:
                        return False
                    sw[j] = 1
                else:
                    return False
    return True

n, l = map(int, sys.stdin.readline().split())
graph = []
cnt = 0
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
for i in graph:
    if check(i):
        cnt += 1
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(graph[j][i])
    if check(tmp):
        cnt += 1
print(cnt)