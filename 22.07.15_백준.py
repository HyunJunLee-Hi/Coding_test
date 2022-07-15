#11054 가장 긴 바이토닉 부분 수열
import sys
import copy

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
# lst_minus = []
# for i in lst:
#     lst_minus.append(i*(-1))
lst_reverse = copy.deepcopy(lst)
lst_reverse.reverse()

dp_a = [1]*n
dp_d = [1]*n

# for i in range(len(lst)-1, -1, -1):
#     if lst[i] == max(lst):
#         max_idx = i
#         break

# for i in range(n):
#     if i <= max_idx:
#         for j in range(i):
#             if lst[i] > lst[j]:
#                 dp[i] = max(dp[i], dp[j] + 1)
#     else:
#         for j in range(i):
#             if lst_minus[i] > lst_minus[j]:
#                 dp[i] = max(dp[i], dp[j] + 1)

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp_a[i] = max(dp_a[i], dp_a[j] + 1)
        if lst_reverse[i] > lst_reverse[j]:
            dp_d[i] = max(dp_d[i], dp_d[j] + 1)

dp_d.reverse()

for i in range(n):
    dp_a[i] += dp_d[i]

print(max(dp_a)-1)

