//
// To run:
//      gcc 1.c -std=gnu99
//      ./a.out
//
// Problem:
//    If we list all the natural numbers below 10 that are multiples of 3 or 5,
//    we get 3, 5, 6 and 9. The sum of these multiples is 23.
//
//    Find the sum of all the multiples of 3 or 5 below 1000.


#include <stdio.h>
#include <time.h>


int solve(int up_to) {
    int sum = 0;
    for(int i = 0; i < up_to; i++) {
        if ((i % 3 == 0) || (i % 5 == 0)) {
            sum += i;
        }
    }
    return sum;
}

int main() {
    clock_t begin = clock();
    int result = solve(1e3);
    clock_t end = clock();
    double time = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("%d [in %f seconds]", result, time);
}
