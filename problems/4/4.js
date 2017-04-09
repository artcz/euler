
// Problem:
//     A palindromic number reads the same both ways. The largest palindrome
//     made from the product of two 2-digit numbers is 9009 = 91 × 99.
//
//     Find the largest palindrome made from the product of two 3-digit
//     numbers.


is_palindrome = function(n) {
    var num = n.toString(),
        // yes, really, that's real way of reversing string in js
        reversed_num = num.split("").reverse().join("");
    return (num === reversed_num ? true : false);
}


solve = function() {
    var max = 1000,
        largest = 0;

    for(i=100; i < max; i++) {
        for(j=100; j < max; j++) {
            n = i*j;
            if(is_palindrome(n) && n > largest) {
                largest = n;
            }
        }
    }
    return largest
}



// unfortunately the accurracy seems to be only 1ms.
console.time('solver');
console.log(solve());
console.timeEnd('solver');
