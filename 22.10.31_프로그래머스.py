#무지의 먹방 라이브
#다시 풀어보기
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0
    previous = 0
    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    q.sort(key=lambda x: x[1])
    return q[(k - sum_value) % length][1]

#틀린 정답
# def solution(food_times, k):
#     answer = 0
#     idx = 0
#
#     while k + 1:
#         if sum(food_times) == 0:
#             return -1
#
#         if food_times[idx % len(food_times)]:
#             food_times[idx % len(food_times)] -= 1
#             idx += 1
#         else:
#             while True:
#                 idx += 1
#                 if food_times[idx % len(food_times)]:
#                     break
#             food_times[idx % len(food_times)] -= 1
#             idx += 1
#         k -= 1
#     return idx % len(food_times)

