#16928 뱀과 사다리 게임
#다시 풀것
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque([start])
    visited[start] = 1
    while q:
        x = q.popleft()
        for i in range(1, 7):
            nx = x + i
            if nx > 100:
                continue
            cnt = graph[nx]
            if visited[cnt] == 0:
                q.append(cnt)
                visited[cnt] = visited[x] + 1
                if cnt == 100:
                    return

visited = [0]*101
graph = [i for i in range(101)]

n, m = map(int, input().split())

for i in range(n+m):
    a, b = map(int, input().split())
    graph[a] = b

bfs(1)

print(visited[100]-1)
