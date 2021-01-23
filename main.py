from ctypes import *

# C
libc = cdll.LoadLibrary("./c/libcalc.so")

# C++
libcpp = cdll.LoadLibrary("./cpp/libcalc.so")

# Go
libgo = cdll.LoadLibrary("./go/libcalc.so")

# Rust
librust = cdll.LoadLibrary("./rust/target/debug/libcalc.dylib")

if __name__ == "__main__":
    print(libc.add(1, 2))
    print(libcpp.sub(1, 2))
    print(libgo.mul(2, 3))
    print(librust.div(10, 5))
