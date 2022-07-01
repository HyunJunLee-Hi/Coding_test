#괄호 회전하기
def is_right(s):
    temp = []
    flag = 0
    for i in s:
        try:
            if i == '(' or i == '{' or i == '[':
                temp.append(i)
            elif i == ')':
                chk = temp.pop()
                if chk == '(':
                    continue
                else:
                    flag = 1
            elif i == '}':
                chk = temp.pop()
                if chk == '{':
                    continue
                else:
                    flag = 1
            elif i == ']':
                chk = temp.pop()
                if chk == '[':
                    continue
                else:
                    flag = 1
        except:
            flag = 1
    if flag == 1:
        return False
    else:
        return True


def solution(s):
    answer = 0
    s = list(s)
    n = len(s)
    if n % 2 != 0:
        return 0
    for i in range(n):
        if is_right(s):
            answer += 1
        s.append(s.pop(0))
    return answer


#올바른 괄호
def solution(s):
    answer = True
    stack = []
    for i in s:
        try:
            if i == '(':
                stack.append(1)
            elif i == ')':
                stack.pop()
        except:
            return False

    if stack:
        return False

    return True


#이진 변환 반복하기
def reverse(lst):
    temp = []
    for i in range(len(lst)-1, -1, -1):
        temp.append(lst[i])
    return temp

def solution(s):
    answer = []
    zero = 0
    change = 0
    temp = list(map(int, s))
    while True:
        if temp == [1]:
            break
        change += 1
        zero += len(temp) - sum(temp)
        # print(change, zero)
        # print(sum(temp))
        new_temp = []
        sum_temp = sum(temp)
        while sum_temp:
            new_temp.append(sum_temp%2)
            sum_temp = sum_temp // 2
        # print(new_temp)
        temp = reverse(new_temp)
        # print(temp)
    answer.append(change)
    answer.append(zero)
    return answer