#1932 정수 삼각형
import sys

input = sys.stdin.readline

n = int(input())
tree = []

for i in range(n):
    tree.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(tree[i])):
        if j == 0:
            tree[i][j] = tree[i-1][j] + tree[i][j]
        elif j == len(tree[i]) - 1:
            tree[i][j] = tree[i-1][j-1] + tree[i][j]
        else:
            tree[i][j] = max(tree[i-1][j], tree[i-1][j-1]) + tree[i][j]
print(max(tree[n-1]))

#11053 가장 긴 증가하는 부분 순열
#한번 더 풀자
import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))


#2565 전깃줄
#한번 더 풀기
#이런 아이디어는 어떻게 생각날까?
import sys

input = sys.stdin.readline

n = int(input())
line = []
dp = [1] * n
for i in range(n):
    line.append(list(map(int, input().split())))

line.sort(key = lambda x : x[1])

for i in range(n):
    for j in range(i):
        if line[i][0] > line[j][0]:
            dp[i] = max(dp[i], dp[j]+1)
print(n - max(dp))

