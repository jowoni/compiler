#include <stdio.h>
#include <stdlib.h>

int queue[5];
int top = 0;

void queue_push() {
    int n;
    int i;
    if (top < 5) {
        top++;
        for (i = top - 1; i > 0; i--) {
            queue[i] = queue[i - 1];
        }
        printf("\ninput : ");
        scanf("%d", &n);
        queue[0] = n;
    } else {
        printf("Queue overflow!\n");
    }
}

void queue_pop() {
    if (top == 0) {
        printf("Empty\n\n");
    } else {
        top--;
        printf("pop : %d\n\n", queue[top]);
    }
}

void queue_print() {
    int i;
    for (i = 0; i < top; i++) {
        printf("%d ", queue[i]);
    }
}

int main(void) {
    int input;
    while (1) {
        printf("\n\n1.Push (max 5) \n2.pop\n");
        scanf("%d", &input);
        if (input == 1) {
            queue_push();
            break;
        }
        if (input == 2) {
            queue_pop();
            break;
        }
        queue_print();
    }
}
