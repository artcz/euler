
// To run:
//     node 3.js
//
// Problem:
//     The prime factors of 13195 are 5, 7, 13 and 29.
//
//     What is the largest prime factor of the number 600851475143 ?
//


largest_factor = function(n) {
    var largest = 0;
    for(i=2; i<=n; i++) {
        if (n%i == 0 && i > largest) {
            largest = i;
            n /= i;
        }
    }
    return largest
}

solve = function() {
    number = 600851475143;
    return largest_factor(number);
}

console.time('solver');
console.log(solve());
console.timeEnd('solver');
