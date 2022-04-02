#12904 A와 B
#t를 s로 변경
import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())
while len(t) != len(s):
    if t[-1] == 'A':
        t.pop()
    else:
        t.pop()
        t.reverse()
if t == s:
    print(1)
else:
    print(0)
