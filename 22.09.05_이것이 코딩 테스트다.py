#큰 수의 법칙
import sys
input = sys.stdin.readline

answer = 0
n, m, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse=True)

cnt = m//(k+1)*k
cnt += m%(k+1)

answer += cnt * lst[0]
answer += (m-cnt) * lst[1]
print(answer)

#13305 주유소
#틀린 답안
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# distance = list(map(int, input().split()))
# price = list(map(int, input().split()))
# real_price = price[:-1]
# real_price.sort()
# cnt = 0
# oil = 0
# answer = 0
# cur = 0
# city = 0
# while sum(distance) >= cnt:
#     if oil < distance[city]:
#         if price[city] == real_price[0]:
#             answer += (sum(distance)-cnt)*real_price[0]
#             break
#         else:
#             answer += price[city]*distance[city]
#             oil += distance[city]
#     else:
#         oil -= distance[city]
#         city += 1
#         cnt += distance[city]
# print(answer)