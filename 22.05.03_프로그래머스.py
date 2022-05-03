#124나라의 숫자
#한 발자국만 더..
def solution(n):
    answer = ''
    if n == 1:
        return '1'
    while n:
        n -= 1
        if n % 3 == 2:
            answer += str(n % 3 + 2)
        else:
            answer += str(n % 3 + 1)
        n = n // 3
    ans = ''
    for i in range(len(answer) - 1, -1, -1):
        ans += answer[i]

    return ans


