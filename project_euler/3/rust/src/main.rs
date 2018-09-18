
fn largest_prime_factor(mut number: u64) -> u64 {
	let mut highest_prime_factor = 1;
	while number % 2 == 0 {
		highest_prime_factor = 2;
		number /= 2;
	}

	for n in 3..(number as f64).sqrt().floor() as u64 {
		while number % n == 0 {
			highest_prime_factor = n;
			number /= n;
		}
	}

	if highest_prime_factor == 1 {
		highest_prime_factor = number;
	}

	return highest_prime_factor;
}

fn main() {
	println!("{}", largest_prime_factor(600851475143));
}
