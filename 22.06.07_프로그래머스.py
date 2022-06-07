#숫자블록
#효율성 다시 생각해보기
def solution(begin, end):
    answer = [0 for _ in range(end + 1)]
    for i in range(1, end // 2 + 1):
        for j in range(2, end // i + 1):
            answer[i * j] = i

    return answer[begin:end + 1]

