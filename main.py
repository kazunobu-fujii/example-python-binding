import ctypes
import numpy as np

# C
libc = ctypes.cdll.LoadLibrary("./c/libcalc.so")

# C++
libcpp = ctypes.cdll.LoadLibrary("./cpp/libcalc.so")

# Go
libgo = ctypes.cdll.LoadLibrary("./go/libcalc.so")

# Rust
librust = ctypes.cdll.LoadLibrary("./rust/target/debug/libcalc.dylib")

if __name__ == "__main__":
    print(f'c.add -> {libc.add(1, 2)}')
    print(f'cpp.sub -> {libcpp.sub(1, 2)}')
    print(f'go.mul -> {libgo.mul(2, 3)}')
    print(f'rust.div -> {librust.div(10, 5)}')

    N = 10
    buf = bytearray(N)
    array = ctypes.c_byte * N

    # C
    libc.sequence(array.from_buffer(buf), N)
    a = np.frombuffer(buf, dtype=np.uint8)
    print(f'c.sequence.sum -> {np.sum(a)}')

    # Go
    libgo.sequence(array.from_buffer(buf), N)
    a = np.frombuffer(buf, dtype=np.uint8)
    print(f'go.sequence.sum -> {np.sum(a)}')

    # Rust
    librust.sequence(array.from_buffer(buf), N)
    a = np.frombuffer(buf, dtype=np.uint8)
    print(f'rust.sequence.sum -> {np.sum(a)}')
