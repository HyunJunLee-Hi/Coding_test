#네트워크
def dfs(graph, visited, n, i):
    visited[i] = 1
    for j in range(n):
        if i != j and graph[i][j] == 1 and visited[j] == 0:
            dfs(graph, visited, n, j)
def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    for i in range(n):
        if visited[i] == 0:
            dfs(computers, visited, n, i)
            answer += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))


#교점에 별 만들기
#한번 더 풀기
def function(line1, line2):
    A, B, C = line1
    a, b, c = line2
    if (A * b) - (B * a) == 0:
        return False
    else:
        x = ((B * c) - (C * b)) / ((A * b) - (B * a))
        y = ((C * a) - (A * c)) / ((A * b) - (B * a))
        if int(x) == x and int(y) == y:
            return int(x), int(y)
        else:
            return False


def solution(line):
    point = []
    n = len(line)
    for i in range(n):
        for j in range(i, n):
            if function(line[i], line[j]):
                x, y = function(line[i], line[j])
                point.append([x, y])
    # max_x = point
    # max_y = point
    # max_x.sort(reverse=True, key = lambda x : abs(x[0]))
    # max_y.sort(reverse=True, key = lambda x : abs(x[1]))
    # print(point)
    # print(abs(max_x[0][0]))
    # print(abs(max_y[0][1]))
    xs = [p[0] for p in point]
    x_min = min(xs)
    x_max = max(xs)

    # 교점의 y좌표들
    ys = [p[1] for p in point]
    y_min = min(ys)
    y_max = max(ys)

    answer = ['.' * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]
    for i, j in point:
        answer[y_max - j] = answer[y_max - j][:i - x_min] + '*' + answer[y_max - j][i - x_min + 1:]

    return answer
