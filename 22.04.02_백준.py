#12904 A와 B
#t를 s로 변경
import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())
while len(t) != len(s):
    if t[-1] == 'A':
        t.pop()
    else:
        t.pop()
        t.reverse()
if t == s:
    print(1)
else:
    print(0)

#2636 치즈
import sys
from collections import deque

def bfs(a, b):
    q = deque()
    q.append([a, b])
    visited[a][b] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < r and 0 <= ny < c:
                if visited[nx][ny] == 0:
                    if graph[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append([nx, ny])
                    else:
                        graph[nx][ny] = 0
                        visited[nx][ny] = 1
                        cnt += 1
    res.append(cnt)
    return cnt

input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
for i in range(r):
    graph.append(list(map(int, input().split())))
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
res = []
time  = 0
while True:
    time += 1
    visited = [[0] * c for _ in range(r)]
    cnt = bfs(0, 0)
    if cnt == 0:
        break
print(time-1)
print(res[-2])

