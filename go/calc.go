package main

import (
	"C"
	"unsafe"
)

//export mul
func mul(a int, b int) int {
	return a * b
}

//export sequence
func sequence(ptr *byte, n int) {
	p := unsafe.Pointer(ptr)
	for i := 0; i < n; i++ {
		*(*byte)(unsafe.Pointer(uintptr(p) + uintptr(i))) = byte(i)
	}
}

func init() {}

func main() {}
