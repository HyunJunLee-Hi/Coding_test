#1105
import sys
input = sys.stdin.readline

l, r = input().split()
l = list(l)
r = list(r)
cnt = 0


if len(l) != len(r):
    print(0)
else:
    for i in range(len(l)):
        if l[i] == r[i]:
            if l[i] == '8':
                cnt += 1
        else:
            break

    print(cnt)

