#문자열 압축
def solution(s):
    n = len(s)
    answer = n
    for i in range(1, n // 2 + 1):
        temp = ''
        chk = s[:i]
        cnt = 1
        for j in range(i, n, i):
            if chk == s[j:j + i]:
                cnt += 1
            else:
                if cnt > 1:
                    temp += str(cnt) + chk
                else:
                    temp += chk
                chk = s[j:j + i]
                cnt = 1
        if cnt > 1:
            temp += str(cnt) + chk
        else:
            temp += chk
        answer = min(answer, len(temp))

    return answer

