#1107 리모컨
#다시 풀어보기
import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
button = list(map(int, input().split()))

answer = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)
    for i in range(len(nums)):
        if int(nums[i]) in button:
            break
        elif i == len(nums) - 1:
            answer = min(answer, abs(int(nums) - target) + len(nums))
print(answer)
# import sys
# import copy
# input = sys.stdin.readline
#
# n = int(input())
# target = list(str(n))
# m = int(input())
# button = list(map(int, input().split()))
# answer = abs(n - 100)
# # 윗 채널
# res_up = 0
# res_down = 0
# cnt_up = 0
# cnt_down = 0
# for i in range(len(target)):
#     temp = copy.deepcopy(target)
#     if int(temp[i]) not in button:
#         res_up += 1
#     else:
#         cnt_up += 1
#         up = copy.deepcopy(temp[i])
#         up = int(up)
#         for _ in range(500001):
#             if up < 9:
#                 up = up + 1
#             else:
#                 break
#             if up not in button:
#                 temp[i] = str(up)
#                 break
#         if _ == 500001:
#             answer = 0
# temp_up = ""
# for i in temp:
#     temp_up += i
# for i in range(len(target)):
#     temp = copy.deepcopy(target)
#     if int(temp[i]) not in button:
#         res_down += 1
#     else:
#         cnt_down += 1
#         down = copy.deepcopy(temp[i])
#         down = int(up)
#         for _ in range(500001):
#             if down != 0: #채널 0에서 -를 누른 경우에는 채널이 변하지 않고
#                 down = down - 1
#             else:
#                 down = 0
#             if down not in button:
#                 temp[i] = str(down)
#                 break
#         if _ == 500001:
#             answer = 0
# temp_down = ""
# for i in temp:
#     temp_down += i
# temp = min(abs(n-int(temp_up))+res_up+cnt_up, abs(n-int(temp_down))+res_down+cnt_down)
# answer = min(answer, temp)
# print(answer)
