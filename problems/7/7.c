// gcc 7.c -std=c11 -lm
//
// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
// that the 6th prime is 13.
//
// What is the 10 001st prime number?


#include <stdio.h>
#include <time.h>
#include <math.h>

#define TRUE 1
#define FALSE 0


int solve() {
    int prime_count = 2, number = 2, is_prime = FALSE;

    while(1) {
        // going to j <= number will make outer while endless, since is_prime
        // will always end up as FALSE. If you don't want to use sqrt(number)
        // go with < instead of <= ;)
        for(int j = 2; j <= sqrt(number); j++) {
            if(number % j == 0) {
                is_prime = FALSE;
                break;
            } else {
                is_prime = TRUE;
            }
        }

        if(is_prime) {
            prime_count++;
            if(prime_count == 10001) {
                return number;
            }
        }

        number += 1;
    }
}


int main() {
    clock_t begin = clock();
    int result = solve();
    clock_t end = clock();
    double time = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("%d [in %f seconds]", result, time);
}
