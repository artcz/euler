
// Each new term in the Fibonacci sequence is generated by adding the previous
// two terms. By starting with 1 and 2, the first 10 terms will be:
// 
// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
// 
// By considering the terms in the Fibonacci sequence whose values do not
// exceed four million, find the sum of the even-valued terms.


#include <stdio.h>
#include <time.h>


int solve() {
    int sum = 0,
        prev = 1,
        goal = 4e6,
        temp;

    for(int i=1; i<=goal;) {
        if(i % 2 == 0) {
            sum += i;
        }
        temp = prev;
        prev = i;
        i += temp;
    }
    return sum;
}


int main() {
    clock_t begin = clock();
    int result = solve();
    clock_t end = clock();
    double time = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("%d [in %f seconds]", result, time);
}
