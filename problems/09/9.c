
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


int solve() {
    for(int c = 5; c < 500; c++)
        for(int b = 1; b < c; b++)
            for(int a = 1; a < b; a++)
                if (a + b + c == 1000 && a*a + b*b == c*c)
                    return a * b *c;
}


int main() {
    clock_t begin = clock();
    int result = solve();
    clock_t end = clock();
    double time = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("%d [in %f seconds]", result, time);
}
