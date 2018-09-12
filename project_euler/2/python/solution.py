#!/usr/bin/env python3.7


def sum_even_fibonacci_numbers_under_limit(
    limit: int,
) -> int:
    a, b, total_sum = 1, 1, 0
    while a <= limit:
        if a % 2 == 0:
            total_sum += a
        a, b = b + a, a
    return total_sum


if __name__ == '__main__':
    print(
        sum_even_fibonacci_numbers_under_limit(
            limit=4_000_000
        )
    )
