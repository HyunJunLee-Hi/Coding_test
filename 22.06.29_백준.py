#1374 강의실
#NameError...
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
lecture = []
for i in range(n):
    lecture.append(list(map(int, input().split())))
#lecture.sort(key=lambda x: (x[1], x[2]))
lecture.sort(key=lambda x : x[2])
lecture = deque(lecture)
answer = 0
while lecture:
    x = lecture.popleft()
    i = len(lecture) - 1
    while i > 0:
        if lecture[i][1] >= x[2]:
            del lecture[i]
            i -= 1
        i -= 1
    answer += 1
print(answer)