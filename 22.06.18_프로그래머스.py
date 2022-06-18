#[1차] 뉴스 클러스터링
#Counter를 배워보자
# def solution(str1, str2):
#     answer = 0
#     str1 = str1.lower()
#     str2 = str2.lower()
#     str_1 = []
#     str_2 = []
#     for i in range(len(str1) - 1):
#         temp = ''
#         temp1 = str1[i]
#         temp2 = str1[i + 1]
#         if 97 <= ord(temp1) <= 122 and 97 <= ord(temp2) <= 122:
#             temp += (temp1 + temp2)
#             str_1.append(temp)
#         else:
#             continue
#     for i in range(len(str2) - 1):
#         temp = ''
#         temp1 = str2[i]
#         temp2 = str2[i + 1]
#         if 97 <= ord(temp1) <= 122 and 97 <= ord(temp2) <= 122:
#             temp += (temp1 + temp2)
#             str_2.append(temp)
#         else:
#             continue
#     print(str_1)
#     print(str_2)
#     print((set(str_1 + str_2)))
#     cnt = 0
#     for i in set(str_1):
#         if i in set(str_2):
#             cnt += 1
#     if len(set(str_1 + str_2)) != 0:
#         print(cnt)
#         print(len(set(str_1 + str_2)))
#         answer = int(65536 * cnt / len(set(str_1 + str_2)))
#
#     else:
#         answer = 65536
#
#     return answer


from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    str_1 = []
    str_2 = []

    for i in range(len(str1) - 1):
        temp = ''
        temp1 = str1[i]
        temp2 = str1[i + 1]
        if 97 <= ord(temp1) <= 122 and 97 <= ord(temp2) <= 122:
            temp += (temp1 + temp2)
            str_1.append(temp)
        else:
            continue
    for i in range(len(str2) - 1):
        temp = ''
        temp1 = str2[i]
        temp2 = str2[i + 1]
        if 97 <= ord(temp1) <= 122 and 97 <= ord(temp2) <= 122:
            temp += (temp1 + temp2)
            str_2.append(temp)
        else:
            continue

    Counter1 = Counter(str_1)
    Counter2 = Counter(str_2)
    print(Counter1)
    print(Counter2)
    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())
    print(inter)
    print(union)
    print(list((Counter1 & Counter2)))
    print(list((Counter1 | Counter2)))
    if len(inter) == 0 and len(union) == 0:
        answer = 65536
    else:
        answer = int(65536*len(inter)/len(union))
    return answer

print(solution("FRANCE", "french"))