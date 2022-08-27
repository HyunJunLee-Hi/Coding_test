#1759 암호 만들기
import sys
from itertools import combinations
input = sys.stdin.readline

l, c = map(int, input().split())
lst = list(input().split())

lst.sort()
res = list(combinations(lst, l))
chk = ['a', 'e', 'i', 'o', 'u']
# idx = 0
# while idx < len(res):
#     if len(set(res[idx]) - set(chk)) == 5:
#         res.pop(idx)
#         idx += 1
#     idx += 1
for i in res:
    cnt = 0
    for j in chk:
        if j in i:
            cnt += 1
    if cnt > 0 and l - cnt > 1:
        print(''.join(i))
#
# answer = []
# for word in res:
#     print(("".join(word)))





