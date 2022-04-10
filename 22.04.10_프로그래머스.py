#점프와 순간 이동
def solution(n):
    ans = 0

    while n:
        if n % 2 == 0:
            n /= 2
        else:
            ans += 1
            n = n // 2

    return ans


