#선택 정렬
import sys
input = sys.stdin.readline
lst = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(lst)):
    min_idx = i
    for j in range(i+1, len(lst)):
        if lst[min_idx] > lst[j]:
            min_idx = j
    lst[i], lst[min_idx] = lst[min_idx], lst[i]
print(lst)

#삽입 정렬
import sys
input = sys.stdin.readline
lst = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(lst)):
    for j in range(i, 0, -1):
        if lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
        else:
            break
print(lst)

#퀵 정렬
import sys
input = sys.stdin.readline
lst = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(lst, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and lst[left] <= lst[pivot]:
            left += 1
        while right > start and lst[right] >= lst[pivot]:
            right -= 1
        if left > right:
            lst[right], lst[pivot] = lst[pivot], lst[right]
        else:
            lst[left], lst[right] = lst[right], lst[left]

    quick_sort(lst, start, right-1)
    quick_sort(lst, right+1, end)

quick_sort(lst, 0, len(lst)-1)
print(lst)

#퀵 정렬2
import sys
input = sys.stdin.readline
lst = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[0]
    tail = lst[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

quick_sort(lst)
print(quick_sort(lst))




#위에서 아래로
import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
lst.sort(reverse=True)
for i in lst:
    print(i, end = ' ')

#성적이 낮은 순서대로 학생 출력하기
import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    name, score = input().split()
    lst.append([name, int(score)])
lst.sort(key = lambda x : x[1])
for i in lst:
    print(i[0], end = ' ')


#두 배열의 원소 교체
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = []
for i in range(2):
    lst.append(list(map(int, input().split())))
lst[0].sort()
lst[1].sort(reverse=True)
for i in range(k):
    if lst[0][i] < lst[1][i]:
        lst[0][i], lst[1][i] = lst[1][i], lst[0][i]
    else:
        break
print(sum(lst[0]))