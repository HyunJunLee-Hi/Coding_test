#21610 마법사 상어와 비바라기
import sys
# import numpy as np
input = sys.stdin.readline

def move(cloud, d, r):
    temp_cloud = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == 1:
                # cloud[i][j] = 0 #구름 이동
                temp_cloud[(i+(dx[d]*r))%n][(j+(dy[d]*r))%n] = 1
    cloud = temp_cloud
    return cloud

def rain(graph, cloud):
    target = []
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == 1:
                graph[i][j] += cloud[i][j]
                target.append([i, j])
    return graph, target

def delete_cloud(cloud):
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == 1:
                cloud[i][j] = -1
    return cloud

def water_copy_bug(graph, target):
    for r, c in target:
        for i in range(1, 8, 2):
            if 0 <= r+dx[i] < n and 0 <= c+dy[i] < n:
                if graph[r+dx[i]][c+dy[i]] > 0:
                    graph[r][c] += 1
    return graph

def new_cloud(graph, cloud):
    temp_cloud = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2 and cloud[i][j] != -1:
                temp_cloud[i][j] = 1
                graph[i][j] -= 2
    cloud = temp_cloud
    return cloud

n, m = map(int, input().split())
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0 ,-1]
graph = []
cloud = [[0]*n for i in range(n)]
cloud[n-1][0] = 1
cloud[n-1][1] = 1
cloud[n-2][0] = 1
cloud[n-2][1] = 1
for i in range(n):
    graph.append(list(map(int, input().split())))
for i in range(m):
    # print(np.array(cloud))
    # print(np.array(graph))
    d, r = map(int, input().split())
    d -= 1
    cloud = move(cloud, d, r) # 1
    graph, target = rain(graph, cloud) # 2
    cloud = delete_cloud(cloud) # 3
    graph = water_copy_bug(graph, target)
    cloud = new_cloud(graph, cloud)

answer = 0
for i in range(n):
    answer += sum(graph[i])
print(answer)


#11279 최대 힙
import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []
for i in range(n):
    num = int(input())
    if num == 0:
        if q:
            print(heapq.heappop(q)*(-1))
        else:
            print(0)
    else:
        heapq.heappush(q, num*(-1))


#1927 최소 힙
import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []
for i in range(n):
    num = int(input())
    if num == 0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, num)

