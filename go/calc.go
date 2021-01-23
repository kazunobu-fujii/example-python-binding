package main

import "C"

//export mul
func mul(a int, b int) int {
	return a * b
}

func init() {}

func main() {}
