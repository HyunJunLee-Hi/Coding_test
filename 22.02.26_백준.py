#2644 촌수계산
import sys
from collections import deque
def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        i = q.popleft()
        for j in graph[i]:
            if visited[j] == 0:
                visited[j] = 1
                res[j] = res[i] + 1
                q.append(j)

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n)]
visited = [0]*n
res = [0]*n
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    x -= 1
    y -= 1
    graph[x].append(y)
    graph[y].append(x)
bfs(a-1)
if res[b-1]:
    print(res[b-1])
else:
    print(-1)


#4949 균형잡힌 세상
import sys
from collections import deque

# stack2 = deque()
while True:
    stack = deque()
    sentence = sys.stdin.readline().rstrip()
    if sentence[0] == '.':
        break
    for i in sentence:
        #print(stack1, stack2)
        # print(stack)
        try:
            if i == '[':
                stack.append(1)
            elif i == ']':
                tmp = stack.pop()
                if tmp != 1:
                    stack.append(tmp)
                    break
            elif i == '(':
                stack.append(2)
            elif i == ')':
                tmp = stack.pop()
                if tmp != 2:
                    stack.append(tmp)
                    break
        except:
            stack.append(3)
            break
    # print(stack)
    # print(sentence)
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
