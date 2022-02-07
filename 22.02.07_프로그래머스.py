#JadenCase 문자열 만들기
#capitalize 모르는 함수
#[:-1] 까먹은 방법
#split 활용
def solution(s):
    s = s.lower()
    answer = s.split(" ")
    res = ''
    for i in answer:
        i = i.capitalize()
        res += (i + " ")
    return res[:-1]