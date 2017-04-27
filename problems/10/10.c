// gcc 10.c -lm
// 
// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
//
// Find the sum of all the primes below two million.


#include <stdio.h>
#include <time.h>
#include <math.h>

#define TRUE 1
#define FALSE 0


long solve() {
    long sum = 0;
    int is_prime;

    for(int i=2; i<=2e6; i++){
        for(int j=2; j<=sqrt(i); j++) {
            if(i % j == 0) {
                is_prime = FALSE;
                break;
            } else {
                is_prime = TRUE;
            }
        }
        if(is_prime) {
            sum += i;
        }
    }

    return sum;
}

// TODO: add other implementations (like Eratosthenes)


int main() {
    clock_t begin = clock();
    long result = solve();
    clock_t end = clock();
    double time = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("%ld [in %f seconds]", result, time);
}
