#include <stdio.h>
#include <stdlib.h>

int sum(int left, int right) {
    return left + right;
}

int square(int num) {
    return num * num;
}

int main(void) {
    int a = 10;
    int b = 5;

    int k = sum(a, b);

    printf("%d", square(k));
    return 0;
}