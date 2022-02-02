# #N-Queen
# #다시 한번 풀어보는 것을 추천
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

#행렬의 곱셈
#이런 문제도 어려워하니
def solution(arr1, arr2):
    x = len(arr1)
    y = len(arr2[0])
    z = len(arr2)
    answer = [[0] * y for i in range(x)]
    for i in range(x):
        for j in range(y):
            for k in range(z):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer

print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))