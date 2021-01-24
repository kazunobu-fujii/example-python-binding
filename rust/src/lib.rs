extern crate libc;

#[no_mangle]
pub extern "C" fn div(a: i32, b: i32) -> i32 {
    a / b
}

#[no_mangle]
pub extern "C" fn sequence(buf: *mut libc::c_void, len: i32) {
    let mut vec: Vec<u8> = Vec::with_capacity(len as usize);
    for i in 0..len {
        vec.push((i + 1) as u8)
    }
    unsafe { std::ptr::copy_nonoverlapping(vec.as_ptr(), buf as *mut u8, len as usize) }
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}
