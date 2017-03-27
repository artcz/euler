
// Problem
// description
// goes
// here


#include <stdio.h>
#include <time.h>


int solve() {
}


int main() {
    clock_t begin = clock();
    int result = solve();
    clock_t end = clock();
    double time = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("%d [in %f seconds]", result, time);
}
