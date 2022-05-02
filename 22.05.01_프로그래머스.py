#괄호 회전하기
#날 잡고 한 500문제 풀어야할듯
def solution(s):
    bracket_dict = {')' : '(', '}' : '{', ']' : '['}
    answer = 0
    for i in range(len(s)):
        stack = []
        chk = 0
        for bracket in s:
            if stack == []:
                if bracket in bracket_dict:
                    chk = 1
                    break

            if bracket in bracket_dict:
                if bracket_dict[bracket] != stack[-1]:
                    chk = 1
                    break
                stack.pop()
            else:
                stack.append(bracket)

        if not chk and not stack:
            answer += 1
        s = s[1:] + s[0]
    return answer

print(solution("[](){}"))