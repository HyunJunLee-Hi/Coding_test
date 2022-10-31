import sys
input = sys.stdin.readline

#만들 수 없는 금액
n = int(input())
coin = list(map(int, input().split()))
coin.sort()

target = 1
for x in coin:
    print(x)
    print(target)
    if target < x:
        break
    target += x
print(target)

#볼링공 고르기
from itertools import combinations

n, m = map(int, input().split())
ball = list(map(int, input().split()))
target = list(combinations(ball, 2))
idx = len(target)-1
while idx:
    a, b = target[idx]
    if a == b:
        target.pop(idx)
        idx -= 1
    idx -= 1
print(len(target))

n, m = map(int, input().split())
ball = list(map(int, input().split()))
weights = [0]*11
for i in ball:
    weights[i] += 1

answer = 0
for i in range(1, m+1):
    n -= weights[i]
    answer += weights[i]*n
print(answer)

