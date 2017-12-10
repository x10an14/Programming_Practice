extern crate num;
use num::Float;

pub struct Complex<T> {
    pub re: T,
    pub im: T,
}

impl<T: Clone> Complex<T> {
    fn new(re: T, im: T) -> Complex<T> {
        unimplemented!();
    }

    fn i() -> Complex<T> {
        unimplemented!();
    }

    fn scale(&self, factor: T) -> Complex<T> {
        unimplemented!();
    }

    fn unscale(&self, factor: T) -> Complex<T> {
        unimplemented!();
    }



}


fn main() {
    println!("Hello, world!");
}
