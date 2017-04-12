// To run:
//      go run 1.go
//      or
//      go build 1.go

// Problem:
//      Description

package main

import "fmt"
import "time"


func solve() int {
    var foo = 0
    return foo
}

func main() {
    t1 := time.Now()
    result := solve()
    t2 := time.Since(t1)

    fmt.Println(result, "in", t2);
}
