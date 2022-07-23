#다음 큰 숫자
#sum 보다는 count가 훨씬 빠르다.
def solution(n):
    answer = 0
    temp = list(str(bin(n)))[2:]
    cnt = temp.count('1')
    for i in range(n+1, 1000001):
        if cnt == list(str(bin(i)))[2:].count('1'):
            answer = i
            break
    return answer
