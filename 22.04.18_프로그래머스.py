#가장 큰 수
#lambda 잘 쓰고 싶다.
def solution(numbers):
    answer = ''
    if sum(numbers) == 0:
        return '0'
    lst = list(map(str, numbers))
    lst.sort(reverse=True, key = lambda x : x*3)
    for i in lst:
        answer += i

    return answer

