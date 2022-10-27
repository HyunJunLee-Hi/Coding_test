import sys
input = sys.stdin.readline

#문자열 뒤집기
lst = input().rstrip()
chk_0 = lst.split('1')
chk_1 = lst.split('0')
cnt_0, cnt_1 = 0, 0
for i in chk_0:
    if i != '':
        cnt_0 += 1
for i in chk_1:
    if i != '':
        cnt_1 += 1
print(min(cnt_0, cnt_1))

