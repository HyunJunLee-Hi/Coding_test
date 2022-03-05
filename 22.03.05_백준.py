#1197 최소 스패닝 트리
#Kruskal Algorithm
# 1. 간선들을 정렬
# 2. 간선이 잇는 두 정점의 root를 찾는다.
# 3. 다르다면 하나의 root를 바꾸어 연결 시켜준다.
# Kruskal 알고리즘은 간선들을 정렬해야하기 때문에 간선이 적으면 Kruskal Algorithm 사용
# Kruskal Algorithm 이용
# 1. root를 저장하는 Vroot 배열을 생선한다.(여기서 root는 연결요소 중 가장 작은 값, 처음에는 자기 자신을 저장)
# 2. 간선들(Elist)을 가중치 기준으로 정렬한다.
# 3. 간선들이 이은 두정점을 find함수를 통해 두 root(sRoot, eRoot)를 찾는다.
# 4. 두 root가 다르다면 큰 root값을 작은 root값으로 만들어 연결되게 해준다.
# 5. 가중치를 더한다.
import sys

def find(x):
    # print(x)
    # print(Vroot)
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]

v, e = map(int, sys.stdin.readline().split())
Vroot = [i for i in range(v)]
Elist = []
for i in range(e):
    Elist.append(list(map(int, sys.stdin.readline().split())))
Elist.sort(key = lambda x : x[2])
answer = 0
for a, b, c in Elist:
    sRoot = find(a-1)
    eRoot = find(b-1)
    if sRoot != eRoot:
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        # print(Vroot)
        answer += c
print(answer)


#Reference : https://hillier.tistory.com/54