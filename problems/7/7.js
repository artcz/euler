//     node 7.js

// Problem:
//
// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
// the 6th prime is 13.
//
// What is the 10 001st prime number?

solve = function() {

    // starting from 1 because the loop below will skip '2' as prime, and set
    // '3' as first prime. Setting prime=1 makes it prime number 2.
    var prime = 1, is_prime;

    for(var i=2;;i++) {
        for(var j=2; j<=Math.sqrt(i)+1; j++) {
            if(i % j == 0) {
                is_prime = false;
                break;
            } else {
                is_prime = true;
            }
        }

        if(is_prime) {
            prime++;
            if(prime === 10001) {
                return i
            }
        }
    }
}



// unfortunately the accurracy seems to be only 1ms.
console.time('solver');
console.log(solve());
console.timeEnd('solver');
