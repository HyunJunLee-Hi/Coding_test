#1149 RGB거리
#다시 풀어보기
import sys
input = sys.stdin.readline

n = int(input())
graph = []
dp = [[0]*3 for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(1, n):
        graph[i][0] = min(graph[i-1][1], graph[i-1][2]) + graph[i][0]
        graph[i][1] = min(graph[i-1][0], graph[i-1][2]) + graph[i][1]
        graph[i][2] = min(graph[i-1][1], graph[i-1][0]) + graph[i][2]
print(min(graph[-1][0], graph[-1][1], graph[-1][2]))
