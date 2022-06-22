#12593 Theme Park (Small)
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    answer = 0
    r, k, n = map(int, input().split())
    q = deque(map(int, input().split()))
    for j in range(r):
        temp = 0
        temp_group = deque()
        while True:
            if q:
                group = q.popleft()
            else:
                q = q + temp_group
                break
            if group + temp > k:
                q.appendleft(group)
                q = q + temp_group
                break
            temp += group
            temp_group.append(group)
        answer += temp
    print("Case #" + str(i+1) + ": ", end='')
    print(answer)

