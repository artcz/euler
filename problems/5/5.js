//     node 5.js

// Problem:
//     2520 is the smallest number that can be divided by each of the numbers
//     from 1 to 10 without any remainder.
//
//     What is the smallest positive number that is evenly divisible by all of
//     the numbers from 1 to 20?

solve1 = function() {
    for(i=2520;;i++) {
        for(j=2; j<=20; j++) {
            if(i%j != 0) {
                found = false;
                break;
            }
            found = true;
        }
        if(found) return i;
    }
}

solve2 = function() {
    var i = 2520,
        found = false;

    while(!found) {
        i++;
        for(j=2; j<=20; j++) {
            if(i%j != 0) {
                found = false;
                break;
            }
            found = true;
        }
    }
    return i;
}



// unfortunately the accurracy seems to be only 1ms.
console.time('solver1');
console.log(solve1());
console.timeEnd('solver1');

console.time('solver2');
console.log(solve2());
console.timeEnd('solver2');
