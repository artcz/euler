// To run:
//     node 1.js

// Problem:
//     If we list all the natural numbers below 10 that are multiples of 3 or
//     5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

//     Find the sum of all the multiples of 3 or 5 below 1000.

solve = function(up_to) {
    sum = 0;
    for(i=0; i<up_to; i++) {
        if((i % 3 == 0) || (i % 5 == 0)) {
            sum += i;
        }
    }
    return sum
}



// unfortunately the accurracy seems to be only 1ms.
console.time('solver');
console.log(solve(1e3));
console.timeEnd('solver');
