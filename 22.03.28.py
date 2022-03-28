#17178 줄서기
#sum(lst, []) 이런 방법이!!
#다시 풀 것
import sys
from collections import deque
#input = sys.stdin.readline()

n = int(sys.stdin.readline())
lst = deque()
order = []
for i in range(n):
    tickets = list(sys.stdin.readline().split())
    temp = deque()
    for ticket in tickets:
        alpha, num = ticket.split('-')
        temp.append((alpha, int(num)))
    lst.append(temp)
    order.append(list(temp))
order = deque(sorted(sum(order, [])))

backstage = deque()
while order:
    current = order[0]

    if lst and lst[0] and current == lst[0][0]:
        order.popleft()
        lst[0].popleft()
    elif backstage and current == backstage[-1]:
        order.popleft()
        backstage.pop()
    else:
        if not lst:
            break
        backstage.append(lst[0].popleft())

    if lst and not lst[0] and n >= 2:
        lst.popleft()

if not order:
    print("GOOD")
else:
    print("BAD")