//다 까먹은 C언어 기억 되살리기

//[프로그래머스]
//평균 구하기
// len = sizeof(arr)/sizeof(int)
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

double solution(int arr[], size_t arr_len) {
    double answer = 0;
    double sum = 0;
    for (int i = 0; i < arr_len; i++)
        sum = sum + arr[i];
    answer = sum / arr_len;
    return answer;
}

//콜라츠 추측
//int 4바이트 -2,147,483648 ~ 2,147,483,647
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(long long num) {
    long long answer = 0;
    int cnt = 0;
    bool flag = true;
    while (1) {
        if (num == 1) {
            break;
        }
        cnt++;
        if (cnt > 500) {
            flag = false;
            break;
        }
        if (num % 2 == 0) {
            num = num / 2;
            continue;
        }
        else {
            num = (num * 3) + 1;
            continue;
        }
    }
    if (flag == true)
        answer = cnt;
    else
        return -1;
    return answer;
}

