#외벽 점검
from itertools import permutations
def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer = len(dist)+1
    # print(weak, length, answer)
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            #print(friends)
            cnt = 1
            pos = weak[start]+friends[cnt-1]
            for i in range(start, start+length):
                if pos < weak[i]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    pos = weak[i]+friends[cnt-1]
            answer = min(cnt, answer)
    if answer > len(dist):
        return -1
    else:
        return answer

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))


#줄 서는 방법
import math
def solution(n, k):
    nums = list(range(1, n+1))
    answer = []
    while n:
        tmp = math.factorial(n-1)
        i = (k-1)//tmp
        k = k%tmp
        # print(tmp, i, k)
        answer.append(nums.pop(i))
        n -= 1
    return answer

print(solution(3, 5))

## 다 다시 풀어보는게 좋을 것 같다