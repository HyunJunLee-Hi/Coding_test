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



#5430 AC
#Reverse 시간 줄이는 팁 : Reverse count 후 마지막에만(삭제는 pop과 popleft 혼용)
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for i in range(t):
    func = input().rstrip()
    func = list(func)
    n = int(input())
    lst = input().rstrip()
    lst = lst[1:]
    q = deque()
    temp = ""
    for j in lst:
        if j == ',' or j == ']':
            if temp != "":
                q.append(int(temp))
                temp = ""
            else:
                break
            continue
        else:
            temp += j
    R_flag = 0
    for j in func:
        flag = 0
        if j == 'R':
            # temp = deque()
            # for i in range(n):
            #     temp.appendleft(q[i])
            # q = temp
            R_flag += 1
        elif j == 'D':
            if q:
                if R_flag % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
            else:
                print("error")
                flag = 1
                break
    if R_flag % 2 == 1:
        temp = deque()
        for i in range(len(q)):
            temp.appendleft(q[i])
        q = temp
    if flag == 0:
        res = "["
        n = len(q)
        cnt = 0
        while n-1 > cnt:
            res += str(q.popleft())
            res += ","
            cnt += 1
        if q:
            res += str(q.popleft())
        res += "]"
        print(res)

