#9184 신나는 함수 실행
import sys

input = sys.stdin.readline

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]

    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return dp[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w({}, {}, {}) = {}".format(a, b, c, w(a, b, c)))

#9461 파도반 수열
import sys

input = sys.stdin.readline

def tri_fibo(n, dp):
    if n == 1 or n == 2 or n == 3:
        return 1
    elif dp[n]:
        return dp[n]
    else:
        dp[n] = tri_fibo(n-2, dp) + tri_fibo(n-3, dp)
        return dp[n]

t = int(input())
lst = []
for i in range(t):
    lst.append(int(input().rstrip()))
dp = [0 for _ in range(max(lst)+1)]

for i in range(t):
    print(tri_fibo(lst[i], dp))

#10844 쉬운 계단 수
#다시 풀어볼 것
import sys

input = sys.stdin.readline

n = int(input())
dp = [[0]*10 for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n])%1000000000)
