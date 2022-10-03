# import sys
# import time
# input = sys.stdin.readline
#
# #피보나치 함수 코드
# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     return fibo(x-1) + fibo(x-2)
# start = time.time()
# print(fibo(35))
# print(time.time() - start)
# #피보나치 수열 소스코드(재귀적)
# d = [0] * 100
#
# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     if d[x] != 0:
#         return d[x]
#     else:
#         d[x] = fibo(x-1) + fibo(x-2)
#         return d[x]
#
# start = time.time()
# print(fibo(35))
# print(time.time() - start)
#
# #피보나치 수열 소스코드(반복적)
# d = [0] * 100
#
# d[1] = 1
# d[2] = 1
# n = 99
#
# for i in range(3, n+1):
#     d[i] = d[i-1] + d[i-2]
#
# print(d[n])
#
# #1로 만들기
# n = int(input())
# d = [0] * (n+1)
#
# for i in range(2, n+1):
#     d[i] = d[i-1] + 1
#     if i%2 == 0:
#         d[i] = min(d[i], d[i//2]+1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i // 5] + 1)
# print(d[n])
#
# #개미 전사
# n = int(input())
# warehouse = list(map(int, input().split()))
# d = [0] * 101
# d[0] = warehouse[0]
# d[1] = max(warehouse[0], warehouse[1])
#
# for i in range(2, n):
#     d[i] = max(d[i-1], d[i-2]+warehouse[i])
#
# print(d[n-1])
#
# #바닥 공사
# n = int(input())
# d = [0] * 1001
#
# d[1] = 1
# d[2] = 3
# for i in range(3, n+1):
#     d[i] = (d[i-1] + d[i-2]*2) % 796796
# print(d[n])


#효율적인 화폐 구성
n, m = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
dp = [10001]*(m+1)
dp[0] = 0

for i in range(n):
    for j in range(coin[i], m+1):
        if dp[j-coin[i]] != 10001:
            dp[j] = min(dp[j], dp[j-coin[i]] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])