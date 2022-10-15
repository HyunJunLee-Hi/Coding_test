#14692 통나무 자르기
import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t+1):
    n = int(input())
    if n%2 == 0:
        print("#{} Alice".format(i))
    else:
        print("#{} Bob".format(i))