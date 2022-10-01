#17140 이차원 배열과 연산
#다시 풀어보기
from collections import Counter
def rc():
    max_len = 0
    for j in range(len(graph)):
        temp = [i for i in graph[j] if i != 0]
        temp = Counter(temp).most_common()
        temp.sort(key = lambda x : (x[1], x[0]))
        graph[j] = []
        for x, y in temp:
            graph[j].append(x)
            graph[j].append(y)
        temp_len = len(temp)
        if max_len < temp_len*2:
            max_len = temp_len*2
    for j in range(len(graph)):
        for k in range(max_len - len(graph[j])):
            graph[j].append(0)
        graph[j] = graph[j][:100]


r, c, k = map(int, input().split())
graph = []
for i in range(3):
    graph.append(list(map(int, input().split())))
for i in range(101):
    try:
        if graph[r-1][c-1] == k:
            print(i)
            break
    except:
        pass
    if len(graph) < len(graph[0]):
        graph = list(zip(*graph))
        rc()
        graph = list(zip(*graph))
    else:
        rc()
else:
    print(-1)

# import sys
# input = sys.stdin.readline
#
# r, c, k = map(int, input().split())
# graph = []
# for i in range(3):
#     graph.append(list(map(int, input().split())))
# flag = False
# for cnt in range(100):
#     try:
#         if graph[r-1][c-1] == k:
#             ans = cnt
#             flag = True
#             break
#     except:
#         pass
#     r_len = len(graph)
#     c_len = len(graph[0])
#     if r_len >= c_len: #행의 개수, 열의 개수 Check
#         max_len = 0 #가장 긴 lst 길이 찾기
#         for i in range(r_len):
#             graph[i].sort(reverse=True) #큰 수로 정렬
#             temp = []
#             max_num = graph[i][0]
#             for j in range(max_num, 0, -1):
#                 cnt_num = graph[i].count(j)
#                 if cnt_num != 0:
#                     temp.append(j)
#                     temp.append(cnt_num)
#             graph[i] = temp
#             max_len = max(max_len, len(temp))
#         for i in range(r_len):
#             if len(graph[i]) < max_len:
#                 for j in range(max_len-len(graph[i])):
#                     graph[i].append(0)
#     else:
#         graph = list(zip(*graph))
#         for i in range(len(graph)):
#             graph[i] = list(graph[i])
#         max_len = 0 #가장 긴 lst 길이 찾기
#         for i in range(c_len):
#             graph[i].sort(reverse=True) #큰 수로 정렬
#             temp = []
#             max_num = graph[i][0]
#             for j in range(max_num, 0, -1):
#                 cnt_num = graph[i].count(j)
#                 if cnt_num != 0:
#                     temp.append(j)
#                     temp.append(cnt_num)
#             graph[i] = temp
#             max_len = max(max_len, len(temp))
#         for i in range(c_len):
#             if len(graph[i]) < max_len:
#                 for j in range(max_len-len(graph[i])):
#                     graph[i].append(0)
#         graph = list(zip(*graph))
#         for i in range(len(graph)):
#             graph[i] = list(graph[i])
# if flag == True:
#     print(ans)
# else:
#     print(-1)