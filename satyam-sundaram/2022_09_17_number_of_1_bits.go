// package main

func hammingWeight(a uint32) int {
    c := 0
    for a != 0 {
        a = a&(a-1)
        c++
    }
    return c
}
