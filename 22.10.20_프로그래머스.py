#최고의 집합
def solution(n, s):
    answer = []
    if s < n:
        return [-1]
    for i in range(n):
        answer.append(s//n)
    idx = 0
    for i in range(s%n):
        answer[idx] += 1
        idx += 1
    answer.sort()


    return answer


#베스트앨범
from collections import Counter
def solution(genres, plays):
    answer = []
    g_cnt = {}
    for i in range(len(genres)):
        if genres[i] in g_cnt:
            g_cnt[genres[i]] += plays[i]
        else:
            g_cnt[genres[i]] = plays[i]
    temp = sorted(g_cnt.items(), key = lambda x : x[1], reverse=True)
    total = []
    for i in range(len(plays)):
        total.append([genres[i], plays[i], i])
    total.sort(key = lambda x : (-x[1], x[2]))
    for genre in temp:
        cnt = 0
        for i in range(len(plays)):
            if cnt < 2:
                if total[i][0] == genre[0]:
                    answer.append(total[i][2])
                    cnt += 1
            else:
                break

    return answer