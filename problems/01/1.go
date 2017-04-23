// To run:
//      go run 1.go
//      or
//      go build 1.go

// Problem:
//    If we list all the natural numbers below 10 that are multiples of 3 or 5,
//    we get 3, 5, 6 and 9. The sum of these multiples is 23.
//
//    Find the sum of all the multiples of 3 or 5 below 1000.

package main

import "fmt"
import "time"


func solve() int {
    var sum, up_to int = 0, 1e3
    for i := 0; i < up_to; i++ {
        if i % 3 == 0 || i % 5  == 0 {
            sum += i
        }
    }
    return sum
}

func main() {
    t1 := time.Now()
    result := solve()
    t2 := time.Since(t1)

    fmt.Println(result, "in", t2);
}
