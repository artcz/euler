
// To run:
//     node 2.js
//
// Problem:
//      Each new term in the Fibonacci sequence is generated by adding the
//      previous two terms. By starting with 1 and 2, the first 10 terms will
//      be:
//
//      1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
//
//      By considering the terms in the Fibonacci sequence whose values do not
//      exceed four million, find the sum of the even-valued terms.


solve = function() {
    var sum = 0,
        _i = 1,
        goal = 4e6,
        prev;

    for(i=1; i<=goal; i += prev) {
        if(i % 2 == 0) {
            sum += i;
        }
        prev = _i;
        _i = i;
    }
    return sum
}



// unfortunately the accurracy seems to be only 1ms.
console.time('solver');
console.log(solve());
console.timeEnd('solver');
