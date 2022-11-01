import sys
input = sys.stdin.readline

#럭키 스트레이트
n = list(str(input().rstrip()))
length = len(n)
left = 0
right = 0
for i in range(length//2):
    left += int(n[i])
for i in range(length//2, length):
    right += int(n[i])
if left == right:
    print("LUCKY")
else:
    print("READY")

#문자열 재정렬
s = list(str(input().rstrip()))
temp = 0
temp_lst = []
for i in range(len(s)):
    if 48 <= ord(s[i]) < 58:
        temp += int(s[i])
    else:
        temp_lst.append(s[i])
temp_lst.sort(key = lambda x : ord(x))
answer = "".join(temp_lst)
answer += str(temp)
print(answer)
