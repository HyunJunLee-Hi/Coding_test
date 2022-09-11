#이진 탐색
import sys
input = sys.stdin.readline

def binary_search(lst, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search(lst, target, start, mid-1)
    else:
        return binary_search(lst, target, mid+1, end)

n, target = list(map(int, input().split()))
lst = list(map(int, input().split()))

res = binary_search(lst, target, 0, n-1)
if res == None:
    print("원소가 존재하지 않습니다.")
else:
    print(res+1)


#이진 탐색2
def binary_search(lst, target, start, end):
    if start > end:
        return None
    while start <= end:
        mid = (start+end)//2
        if lst[mid] > target:
            end = mid - 1
        elif lst[mid] == target:
            return mid
        else:
            start = mid + 1
    return None

n, target = list(map(int, input().split()))
lst = list(map(int, input().split()))

res = binary_search(lst, target, 0, n-1)
if res == None:
    print("원소가 존재하지 않습니다.")
else:
    print(res+1)


#부품 찾기
import sys
input = sys.stdin.readline

def binary_search(lst, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search(lst, target, start, mid-1)
    else:
        return binary_search(lst, target, mid+1, end)

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    res = binary_search(lst, target, 0, n-1)
    if res != None:
        print("yes", end = " ")
    else:
        print("no", end = " ")

#계수 정렬
n = int(input())
lst = [0]*1000001

for i in input().split():
    lst[int(i)] = 1
m = int(input())
targets = list(map(int, input().split()))
for target in targets:
    if lst[target]:
        print("yes", end = " ")
    else:
        print("no", end = " ")


#집합 자료형
n = int(input())
lst = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    if target in lst:
        print("yes", end = " ")
    else:
        print("no", end = " ")


#떡볶이 떡 만들기
import sys
input = sys.stdin.readline

def binary_search(lst, target, start, end):
    if start > end:
        return None
    while end >= start:
        mid = (start+end)//2
        temp = 0
        for i in lst:
            if i > mid:
                temp += (i-mid)

        if temp < target:
            end = mid-1
        else:
            res = mid
            start = mid+1
    return res

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

res = binary_search(lst, m, 0, max(lst))
print(res)