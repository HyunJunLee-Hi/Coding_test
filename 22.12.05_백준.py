#14501 퇴사
import sys
import copy
input = sys.stdin.readline

n = int(input())
t = []
p = []
dp = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)
# print(dp)

for i in range(n-1, -1, -1):
    if t[i] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p[i] + dp[i+t[i]])
        # print(dp)
        # print(dp[i], dp[i+t[i]])

# answer = 0
# n = int(input())
# lst = []
# days = [0]*n
# for i in range(n):
#     temp = list(map(int, input().split()))
#     temp.append(i)
#     lst.append(temp)
#
# sorted_lst = copy.deepcopy(lst)
# sorted_lst.sort(reverse = True, key = lambda x : (x[1], -x[0]))
#
# for t, p, idx in sorted_lst:
#     if idx+t < n:
#         for i in range(idx, idx+t):
#             days[i] += 1
#         if t == sum(days[idx:idx+t]):
#             answer += p
#         else:
#             for i in range(idx, idx+t):
#                 days[i] -= 1
#         print(days)
# print(answer)