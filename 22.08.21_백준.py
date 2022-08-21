#2110 공유기 설치
#다시풀기
import sys
input = sys.stdin.readline

def binary_search(start, end):
    while start < end:
        mid = (start+end) // 2
        cur = house[0]
        cnt = 1

        for i in range(1, len(house)):
            if house[i] >= cur + mid:
                cnt += 1
                cur = house[i]
        if cnt >= c:
            global answer
            answer = mid
            start = mid + 1
        else:
            end = mid

n, c = map(int, input().split())
house = []
for i in range(n):
    house.append(int(input()))
house.sort()

start = 1
end = house[-1] - house[0]
answer = 0

if c == 2:
    print(house[-1] - house[0])
else:
    binary_search(start, end)
    print(answer)


# import sys
# import copy
# input = sys.stdin.readline
#
# n, c = map(int, input().split())
# house = []
# distance = []
# for _ in range(n):
#     house.append(int(input()))
# house.sort()
# lan = copy.deepcopy(house)
# for i in range(n-1):
#     distance.append(house[i+1] - house[i])
# for _ in range(n-4):
#     temp = []
#     for i in range(len(distance) - 1):
#         temp.append(distance[i+1] + distance[i])
#     distance = copy.deepcopy(temp)
# print(min(distance))
