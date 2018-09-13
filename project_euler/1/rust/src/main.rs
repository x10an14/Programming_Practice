
fn num_is_divisible_by_numbers(num: u32, numbers: &Vec<u32>) -> bool {
	let mut found = false;
	for x in numbers {
		if num % x == 0 {
			found = true;
			break
		}
	}
	found
}

fn sum_divisible_numbers_under_limit(limit: u32, divisible_nums: &Vec<u32>) -> u32 {
	let mut n = 0;
	let mut sum = 0;
	while n < limit {
		if num_is_divisible_by_numbers(n, divisible_nums) {
			sum += n;
		}
		n += 1;
	}
	sum
}

fn main() {
	println!(
		"{}",
		sum_divisible_numbers_under_limit(
			1000,
			&vec![3, 5]
		)
	);
}
