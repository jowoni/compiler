#include <stdio.h>

int main() {
    int age;


    printf("Enter your age : ");
    scanf("%d", &age);


    if (age <= 6 || age >= 60) {
        printf("Free");
    } else {
        printf("1,000 won");
    }

    return 0;
}
