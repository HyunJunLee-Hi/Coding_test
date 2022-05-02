#위장
#그렇다.
#이젠 경우의 수는 너무 옜날이야...
def solution(clothes):
    answer = 1
    kind_dict = {}
    kind = []
    for cloth in clothes:
        kind.append(cloth[1])
        if cloth[1] in kind_dict:
            kind_dict[cloth[1]].append(cloth[0])
        else:
            kind_dict[cloth[1]] = [cloth[0]]
    kinds = list(set(kind))
    for i in kind_dict.keys():
        answer *= (len(kind_dict[i])+1)
    return answer - 1