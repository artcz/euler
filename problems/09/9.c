
// A Pythagorean triplet is a set of three natural numbers, a < b < c, for
// which,
//
// a² + b² = c²
//
// For example, 3³ + 4² = 9 + 16 = 25 = 5²
//
// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.


#include <stdio.h>
#include <time.h>


int solve1() {
    for(int c = 5; c < 500; c++)
        for(int b = 1; b < c; b++)
            for(int a = 1; a < b; a++)
                if (a + b + c == 1000 && a*a + b*b == c*c)
                    return a * b *c;
}

int solve2() {
    for(int b = 5; b < 500; b++)
        for(int a = 1; a < b; a++) {
#define C (1000 - a - b)
            if(a*a + b*b == C*C)
                return a * b * C;
        }
#undef C
}


int main() {
    clock_t begin = clock();
    int result = solve1();
    clock_t end = clock();
    double time = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("%d [in %f seconds]\n", result, time);

    clock_t begin2 = clock();
    int result2 = solve2();
    clock_t end2 = clock();
    double time2 = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("%d [in %f seconds]\n", result2, time2);
}
