//�� ����� C��� ��� �ǻ츮��

//[���α׷��ӽ�]
//���簢�� �����
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


//�ڵ��� ��ȣ ������
//strlen, strcpy �߾��� �Լ���...
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

//�ϻ��� ��
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