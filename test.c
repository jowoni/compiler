#include <stdio.h>

int main() {
    int num;
    int i;


    printf("Enter the number : ");
    scanf("%d", &num);


    for (i = 2; i < num; i++) {
        printf("%d %% %d = %d\n", num, i, num % i);
        if (num % i == 0) {
            break;
        }
    }


    if (i == num) {
        printf("Prime");
    } else {
        printf("Not Prime");
    }


    return 0;
}
