#1697 숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline
history = []
def bfs(start, history):
    q = deque()
    q.append([start])
    cnt = 1
    #visited[start] = 1
    while q:
        target = q.popleft()
        temp = []
        for x in target:
            for i in range(3):
                if i == 0:
                    nx = x-1
                    if 0 <= nx <= 100000:
                        if nx == k:
                            return cnt
                        if nx not in history:
                            temp.append(nx)
                            history.append(nx)
                elif i == 1:
                    nx = x+1
                    if 0 <= nx <= 100000:
                        if nx == k:
                            return cnt
                        if nx not in history:
                            temp.append(nx)
                            history.append(nx)
                else:
                    nx = x*2
                    if 0 <= nx <= 100000:
                        if nx == k:
                            return cnt
                        if nx not in history:
                            temp.append(nx)
                            history.append(nx)
        cnt += 1
        q.append(temp)
    return cnt

n, k = map(int, input().split())
if n == k:
    print(0)
else:
    history.append(n)
    print(bfs(n, history))



#2002 추월
#다시 풀어보기
import sys
input = sys.stdin.readline

n = int(input())
dae = {}
young = []

for i in range(n):
    dae[str(input())] = i
for i in range(n):
    young.append(str(input()))

cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        if dae[young[i]] > dae[young[j]]:
            cnt += 1
            break
print(cnt)

