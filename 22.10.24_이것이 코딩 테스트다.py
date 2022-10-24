import sys
input = sys.stdin.readline

#모험가 길드
n = int(input())
lst = list(map(int, input().split()))
lst.sort()

cnt = 0
answer = 0
for i in lst:
    cnt += 1
    if cnt == i:
        cnt = 0
        answer += 1
print(answer)

#곱하기 혹은 더하기
number = list(map(int, input().rstrip()))
if sum(number) != 0:
    answer = 1
    for i in range(len(number)):
        if int(number[i]) == 0:
            continue
        else:
            answer *= int(number[i])
else:
    answer = 0
print(answer)

