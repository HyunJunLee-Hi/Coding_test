#11057 오르막 수
# import sys
# input = sys.stdin.readline
#
# n = int(input())
#
# if n == 1:
#     res = 10
# else:
#     start = 10**(n-1)
#     end = 10**n
#     res = 1
#     for target in range(start, end):
#         flag = 0
#         temp = target%10
#         while target:
#             if temp > target%10:
#                 flag = 1
#                 break
#             else:
#                 temp = target%10
#                 target = target // 10
#         if flag == 0:
#             res += 1
# print(res%10007)
# import sys
# input = sys.stdin.readline
# n = int(input())
# dp = [[0]*10 for i in range(1001)]
# for i in range(10):
#     dp[1][i] = 1
# for i in range(2, 1001):
#     for j in range(10):
#         for k in range(j+1):
#             dp[i][j] += dp[i-1][k]
#
# print(sum(dp[n])%10007)


#4948 베르트랑 공준
# import sys
# import math
# input = sys.stdin.readline
#
# def is_prime(n):
#     if n == 1:
#         return False
#     for i in range(2, int(math.sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True
#
# lst = []
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     else:
#         lst.append(n)
#
# for n in lst:
#     res = 0
#     for i in range(n+1, n*2+1):
#         if is_prime(i):
#             res += 1
#     print(res)

#1931 회의실 배정
import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
lst.sort(key = lambda x : x[0])
lst.sort(key = lambda x : x[1])
sch = [lst[0]]
cnt = 0
last = 0
for i, j in lst:
    # print(target[0], sch[-1][1])
    # if i >= sch[-1][1]:
    #     sch.append(target)
        # print(sch)
    if i >= last:
        cnt += 1
        last = j
print(cnt)