#[macro_use] extern crate cached;
#[macro_use] extern crate lazy_static;

// Ref. https://github.com/jaemk/cached/blob/0ed46ce9d6/README.md
cached!{
	FIB;
	fn fib(n: u64) -> u64 = {
		if n == 0 || n == 1 { return 1}
		fib(n - 1) + fib(n - 2)
	}
}

fn sum_even_fibonacci_under_limit(limit: u64) -> u64 {
	let mut sum = 0;

	let mut current_index = 0;
	let mut fib_n = fib(current_index);

	while fib_n < limit {
		if fib_n % 2 == 0 {
			sum += fib_n;
		}
		current_index += 1;
		fib_n = fib(current_index)
	}
	sum
}

fn main() {
	println!(
		"{}",
		sum_even_fibonacci_under_limit(
			4000000u64
		)
	);
}
