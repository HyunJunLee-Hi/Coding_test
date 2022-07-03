#스티커 모으기(2)
#실패 + 시간초과
from itertools import combinations

def solution(sticker):
    answer = 0
    target = len(sticker) // 2

    candidates = list(combinations(sticker, target))
    for candidate in candidates:
        idx_lst = []
        for i in range(len(candidate)):
            idx_lst.append(sticker.index(candidate[i]))
        idx_lst.sort()
        flag = 0
        for i in range(len(idx_lst)):
            if abs((idx_lst[i] - idx_lst[i - 1]) % len(sticker)) < 2:
                flag = 1
                break
        if flag == 0:
            answer = max(answer, sum(candidate))

    return answer

