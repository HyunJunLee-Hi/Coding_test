#최고의 집합
def solution(n, s):
    answer = []
    if s // n < 1:
        return [-1]

    a, b = divmod(s, n)
    answer = [a] * n
    for i in range(b):
        answer[i] += 1
    answer.sort()

    return answer

print(solution(2, 9))


#줄 서는 방법
## 시간초과
from itertools import permutations
def solution(n, k):
    answer = []
    tmp = []
    for i in range(1, n + 1):
        tmp.append(i)
    lst = list(permutations(tmp, n))
    answer = lst[k - 1]

    return answer

