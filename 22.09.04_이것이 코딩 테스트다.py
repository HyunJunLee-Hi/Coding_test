#큰 수의 법칙
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
chk = 0
idx = 0
flag = True
answer = 0
for i in range(m):
    if flag == False:
        idx -= 1
        flag = True
    answer += lst[idx]
    chk += 1
    if chk == k:
        idx += 1
        flag = False
print(answer)

#숫자 카드 게임
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
target = []
for i in range(n):
    target.append(min(graph[i]))
target.sort(reverse=True)
print(target[0])


#1이 될 떄까지
import sys
input = sys.stdin.readline

answer = 0
n, k = map(int, input().split())
while True:
    # print(n)
    if n == 1:
        break
    if n % k == 0:
        answer += 1
        n = n//k
    else:
        answer += 1
        n -= 1
print(answer)