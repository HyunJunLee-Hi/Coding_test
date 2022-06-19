#2개 이하로 다른 비트
#신기한 함수가 많다.
#rfind, int('2진수', 2)
def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            temp = str(bin(num))
            temp = '0' + temp[2:]
            idx = temp.rfind('0')
            temp = list(temp)
            temp[idx] = '1'
            temp[idx + 1] = '0'
            answer.append(int(''.join(temp), 2))

    return answer


