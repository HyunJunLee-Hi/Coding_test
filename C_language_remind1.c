//다 까먹은 C언어 기억 되살리기

//[프로그래머스]
//직사각형 별찍기
#include <stdio.h>
int main(void) {
    int n;
    int m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}


//핸드폰 번호 가리기
//strlen, strcpy 추억의 함수다...
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* phone_number) {
    int len = strlen(phone_number);
    char* answer = (char*)malloc(len);
    strcpy(answer, phone_number);
    for (int i = 0; i < len - 4; i++) {
        answer[i] = '*';
    }
    return answer;
}

//하샤드 수
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
    bool answer = true;
    int sum = 0;
    int y = x;
    while (x > 0) {
        sum = sum + (x % 10);
        x = x / 10;
    }
    if (y % sum != 0)
        answer = false;
    return answer;
}