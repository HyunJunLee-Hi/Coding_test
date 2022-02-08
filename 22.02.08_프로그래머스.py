#brute force
from itertools import permutations
def solution(k, dungeons):
    answer = -1
    cases = list(permutations(dungeons, len(dungeons)))
    for case in cases:
        tmp = k
        cnt = 0
        for i in case:
            if tmp >= i[0]:
                tmp -= i[1]
                cnt += 1
        if answer <= cnt:
            answer = cnt
    return answer
