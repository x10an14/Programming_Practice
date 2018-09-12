#!/usr/bin/env python3.7

from typing import Iterable


def num_divisble_by_numbers(
    num: int,
    numbers: Iterable[int],
) -> bool:
    for x in numbers:
        if num % x == 0:
            return True
    return False


def sum_divisible_numbers_under_limit(
    divisble_numbers: Iterable[int],
    limit: int,
) -> int:
    n, total_sum = 0, 0
    while n < limit:
        if num_divisble_by_numbers(n, divisble_numbers):
            total_sum += n
        n += 1
    return total_sum


if __name__ == '__main__':
    print(
        sum_divisible_numbers_under_limit(
            divisble_numbers=(3, 5),
            limit=1000,
        )
    )
