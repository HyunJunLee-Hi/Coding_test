#1158 요세푸스 문제
# import sys
# from collections import deque
#
# q = []
# n, k = map(int, sys.stdin.readline().split())
# res = []
# for i in range(1, n+1):
#     q.append(i)
# cur = k - 1
# while q:
#     res.append(q.pop(cur))
#     if len(q) == 0:
#         break
#     else:
#         cur = (cur-1+k) % len(q)
# print('<', end='')
# for i in range(n-1):
#     print(res[i], end=', ')
#
# print(str(res[n-1]) + '>')


#1292 쉽게 푸는 문제
#Runtime Error(IndexError)
#a=b인 경우
import sys

a, b = map(int, sys.stdin.readline().split())
lst = []
for i in range(1, b+1):
    for j in range(i):
        lst.append(i)
res = 0
for i in range(a-1, b):
    res += lst[i]
print(res)