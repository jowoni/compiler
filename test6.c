#include <stdio.h>
#include <cstdlib>

int is_power_of_two(int n) {
    return ((n > 0) && !(n & (n - 1)));
}

int main(void) {
    int num = 100;
    printf("%d\n", is_power_of_two(num));
}