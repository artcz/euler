//     node 6.js

// Problem:
//
// The sum of the squares of the first ten natural numbers is,
//
// 1² + 2² + ... + 10² = 385
//
// The square of the sum of the first ten natural numbers is,
//
// (1 + 2 + ... + 10)² = 552 = 3025
//
// Hence the difference between the sum of the squares of the first ten natural
// numbers and the square of the sum is 3025 − 385 = 2640.
//
// Find the difference between the sum of the squares of the first one hundred
// natural numbers and the square of the sum.

solve = function() {
    var sum = 0,
        sum_of_squares = 0,
        N = 100,
        result;

    for(i=0; i<=N; i++){
        sum += i;
        sum_of_squares += i*i;
    }

    result = sum_of_squares - sum*sum;
    return Math.abs(result)
}



// unfortunately the accurracy seems to be only 1ms.
console.time('solver');
console.log(solve());
console.timeEnd('solver');
