#N-Queen
#다시 한번 풀어보는 것을 추천
def adjacent(chess, x):
    for i in range(x):
        if chess[x] == chess[i] or abs(chess[x] - chess[i]) == x - i:
            return 0
    return 1

def dfs(chess, n, x): #x는 현재 기준이 되는 row의 index
    global cnt
    if x == n: #끝까지 다 잘 돌았으니 1 증가 가능
        cnt += 1
    else:
        for i in range(n): #기준이 되는 row중 queen 넣어도 괜찮은 자리 찾기
            chess[x] = i
            print(chess)
            if adjacent(chess, x):
                dfs(chess, n, x+1)
    return cnt

def solution(n):
    queen = [0] * n
    global cnt
    cnt = 0
    dfs(queen, n, 0)
    return cnt

print(solution(4))