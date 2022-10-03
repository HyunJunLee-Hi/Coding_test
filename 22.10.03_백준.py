#23291 어항 정리
#이걸 이 시간 안에...?
import sys
import copy
input = sys.stdin.readline

def step1(fishbowl): #물고기의 수가 가장 작은 어항에 물고기를 한 마리 넣는다.
    min_num = min(fishbowl)
    for i in range(n):
        if fishbowl[i] == min_num:
            fishbowl[i] += 1
    return fishbowl

def step2(fishbowl): #90도 어항 쌓기
    temp = copy.deepcopy(fishbowl)
    rot = [[temp[0]], [temp[1]]]
    temp = temp[2:]

    while True:
        h = len(rot)
        w = len(rot[0])
        if h <= len(temp):
            # rot = list(zip(*rot))
            # for i in range(w):
            #     rot[i] = list(rot[i])
            temp_rot = [[0]*h for _ in range(w)]
            for i in range(w):
                for j in range(h):
                    temp_rot[i][j] = rot[h-j-1][i]
            rot = temp_rot + [temp[:h]]
            temp = temp[h:]

        else:
            rot[-1] = rot[-1] + temp
            break
    return rot

def step3(fishbowl): #물고기 수 조절
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    h = len(fishbowl)
    w = len(fishbowl[-1])
    temp = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(len(fishbowl[i])):
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                try:
                    if 0 <= nx < h and 0 <= ny < len(fishbowl[i]):
                        if (fishbowl[i+dx[k]][j+dy[k]]-fishbowl[i][j]) < 0 and (fishbowl[i+dx[k]][j+dy[k]]-fishbowl[i][j])%5 != 0:
                            temp[i][j] += (fishbowl[i+dx[k]][j+dy[k]]-fishbowl[i][j])//5 + 1
                        else:
                            temp[i][j] += (fishbowl[i + dx[k]][j + dy[k]] - fishbowl[i][j])//5
                except:
                    pass
    try:
        for i in range(h):
            for j in range(len(fishbowl[i])):
                fishbowl[i][j] += temp[i][j]
    except:
        pass

    return fishbowl

def step4(fishbowl): #일렬로 만들기
    h = len(fishbowl)
    w = len(fishbowl[-1])
    temp = []
    for i in range(w):
        for j in range(h):
            try:
                temp.append(fishbowl[h-j-1][i])
            except:
                pass

    return temp

def step5(fishbowl): #180도 어항 쌓기
    left = fishbowl[:len(fishbowl)//2]
    left.reverse()
    right = fishbowl[len(fishbowl)//2:]
    temp = []
    temp.append(left)
    temp.append(right)

    left_top = temp[0][:n//4]
    left_bottom = temp[1][:n//4]
    right_top = temp[0][n//4:]
    right_bottom = temp[1][n//4:]
    left_top.reverse()
    left_bottom.reverse()
    temp = []
    temp.append(left_bottom)
    temp.append(left_top)
    temp.append(right_top)
    temp.append(right_bottom)
    return temp

n, m = map(int, input().split())
fishbowl = list(map(int, input().split()))
answer = 0
while True:
    if max(fishbowl) - min(fishbowl) <= m:
        print(answer)
        break
    answer += 1
    fishbowl = step1(fishbowl)
    fishbowl = step2(fishbowl)
    fishbowl = step3(fishbowl)
    fishbowl = step4(fishbowl)
    fishbowl = step5(fishbowl)
    fishbowl = step3(fishbowl)
    fishbowl = step4(fishbowl)
