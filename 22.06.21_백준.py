#21995 King's Task
#틀린 답
import sys
input = sys.stdin.readline

def p1(lst):
    for i in range(0, 2*n-1, 2):
        temp = lst[i]
        lst[i] = lst[i+1]
        lst[i+1] = temp

def p2(lst):
    temp = lst[:n]
    lst[:n] = lst[n:]
    lst[n:] = temp

def is_even_odd(lst):
    for i in range(0, 2*n, 2):
        if lst[i] % 2 != 0:
            return False
    for i in range(1, 2*n+1, 2):
        if lst[i] % 2 == 0:
            return False
    return True

def is_odd_even(lst):
    for i in range(0, 2*n, 2):
        if lst[i] % 2 == 0:
            return False
    for i in range(1, 2*n+1, 2):
        if lst[i] % 2 != 0:
            return False
    return True

n = int(input())
lst = list(map(int, input().split()))
answer = 0
temp = []
for i in lst:
    temp.append(i)
temp.sort()

for i in range(2*n):
    if temp == lst:
        print(answer)
        break
    if lst[0] % 2 == 0 and is_even_odd(lst):
        p1(lst)
        answer += 1
        continue
    elif lst[0] % 2 != 0 and is_odd_even(lst):
        if lst[0] + 1 == lst[-1]:
            p2(lst)
            answer += 1
            continue
        else:
            p1(lst)
            answer += 1
            continue
    else:
        print(-1)
        break
    if i == 2*n -1:
        print(-1)
        break

# import sys
# input = sys.stdin.readline
#
# def p1(lst):
#     for i in range(0, 2*n-1, 2):
#         temp = lst[i]
#         lst[i] = lst[i+1]
#         lst[i+1] = temp
#
# def p2(lst):
#     temp = lst[:n]
#     lst[:n] = lst[n:]
#     lst[n:] = temp
#
# def is_even_odd(lst):
#     for i in range(0, 2*n, 2):
#         if lst[i] % 2 != 0:
#             return False
#     for i in range(1, 2*n+1, 2):
#         if lst[i] % 2 == 0:
#             return False
#     return True
#
# def is_odd_even(lst):
#     for i in range(0, 2*n, 2):
#         if lst[i] % 2 == 0:
#             return False
#     for i in range(1, 2*n+1, 2):
#         if lst[i] % 2 != 0:
#             return False
#     return True
#
# n = int(input())
# lst = list(map(int, input().split()))
# answer = 0
# temp = []
# for i in lst:
#     temp.append(i)
# temp.sort()
#
# for i in range(2*n):
#     if temp == lst:
#         print(answer)
#         break
#     if lst[0] % 2 == 0 and is_even_odd(lst):
#         p1(lst)
#         answer += 1
#         continue
#     elif lst[0] % 2 != 0 and is_odd_even(lst):
#         if lst[0] + 1 == lst[-1]:
#             p2(lst)
#             answer += 1
#             continue
#         else:
#             p1(lst)
#             answer += 1
#             continue
#     else:
#         print(-1)
#         break
#     if i == 2*n -1:
#         print(-1)
#         break

# import sys
# from itertools import permutations
# input = sys.stdin.readline
#
# def p1(lst):
#     for i in range(0, 2*n-1, 2):
#         temp = lst[i]
#         lst[i] = lst[i+1]
#         lst[i+1] = temp
#
# def p2(lst):
#     temp = lst[:n]
#     lst[:n] = lst[n:]
#     lst[n:] = temp
#
# def is_even_odd(lst):
#     for i in range(0, 2*n, 2):
#         if lst[i] % 2 != 0:
#             return False
#     for i in range(1, 2*n+1, 2):
#         if lst[i] % 2 == 0:
#             return False
#     return True
#
# def is_odd_even(lst):
#     for i in range(0, 2*n, 2):
#         if lst[i] % 2 == 0:
#             return False
#     for i in range(1, 2*n+1, 2):
#         if lst[i] % 2 != 0:
#             return False
#     return True
#
# n = int(input())
# # test_num = [i for i in range(1, 2*n+1)]
# # print(test_num)
# # test_lst = list(permutations(test_num, 2*n))
# # print(test_lst)
# lst = list(map(int, input().split()))
# # for lst in test_lst:
# #     lst = list(lst)
# answer = 0
# temp = []
# for i in lst:
#     temp.append(i)
# temp.sort()
#
# for i in range(2*n):
#     if temp == lst:
#         print(answer)
#         break
#     if not is_even_odd(lst) and not is_odd_even(lst):
#         print(-1)
#         break
#     if lst[0] % 2 != 0 and is_even_odd(lst):
#         print(-1)
#         break
#         # p1(lst)
#         # answer += 1
#         # continue
#     elif lst[0] % 2 == 0 and is_odd_even(lst):
#         print(-1)
#         break
#     else:
#         if lst[0] + 1 == lst[-1]:
#             p2(lst)
#             answer += 1
#             continue
#         else:
#             p1(lst)
#             answer += 1
#             continue
#     if i == 2*n-1:
#         print(-1)
# 6 3 2 5 4 1
# 3 6 5 2 1 4
# 2 1 4 3 6 5
# 1 2 3 4 5 6

# 5 4 1 6 3 2

