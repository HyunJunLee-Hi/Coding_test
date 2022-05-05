#2981 검문
#수학도 어렵구나
import sys
import math

input = sys.stdin.readline

n = int(input())
lst = []
target = []
ans = []
for i in range(n):
    lst.append(int(input()))
lst.sort()

for i in range(1, n):
    target.append(lst[i] - lst[i-1])
prev = target[0]

for i in range(1, n-1):
    prev = math.gcd(prev, target[i])

for i in range(2, int(math.sqrt(prev))+1):
    if prev % i == 0:
        ans.append(i)
        ans.append(prev//i)
ans.append(prev)
ans = list(set(ans))
ans.sort()
res = ''
if len(ans) == 1:
    print(str(ans[0]))
else:
    for i in range(len(ans)-1):
        res += str(ans[i]) + ' '
    print(res + str(ans[len(ans)-1]))

# input = sys.stdin.readline
#
# n = int(input())
# lst = []
# ans = []
#
# for i in range(n):
#     lst.append(int(input()))
#
# for i in range(2, max(lst)//2+1):
#     target = lst[0] % i
#     flag = 0
#     for j in lst:
#         if j%i != target:
#             flag = 1
#             break
#     if flag == 0:
#         ans.append(i)
# res = ''
# if len(ans) == 1:
#     print(str(ans[0]))
# else:
#     for i in range(len(ans)-1):
#         res += str(ans[i]) + ' '
#     print(res + str(ans[len(ans)-1]))