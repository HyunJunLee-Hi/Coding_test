#N개의 최소공배수
from math import gcd
def solution(arr):
    answer = arr[0]
    for i in arr:
        print(gcd(answer, i))
        answer = answer*i//gcd(answer, i)
    return answer