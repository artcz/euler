
// To run:
//      gcc 4.c -std=c99
//
// Problem:
//     A palindromic number reads the same both ways. The largest palindrome
//     made from the product of two 2-digit numbers is 9009 = 91 × 99.
//
//     Find the largest palindrome made from the product of two 3-digit
//     numbers.


#include <stdio.h>
#include <time.h>


int is_palindrome(int number) {
    int original = number, reversed = 0;
    while(number > 0) {
        reversed = reversed * 10 + number % 10;
        number /= 10;
    }
    return original == reversed;
}


int solve() {

    int i = 100,
        max = 1000,
        largest = 0;

    while(i < max) {
        int j = 100;
        while(j < max) {
            if (is_palindrome(i*j) && (i*j > largest)) {
                largest = i*j;
            }
            j += 1;
        }
        i += 1;
    }

    return largest;
}


int main() {
    clock_t begin = clock();
    int result = solve();
    clock_t end = clock();
    double time = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("%d [in %f seconds]", result, time);
}
