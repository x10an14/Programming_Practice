#!/usr/bin/env python3.7

from math import sqrt, floor


def largest_prime_factor(
    number: int
) -> int:
    highest_prime_factor = 1

    while number % 2 == 0:
        highest_prime_factor = 2
        number /= 2

    for n in range(3, floor(sqrt(number)), 2):
        while number % n == 0:
            highest_prime_factor = n
            number /= n

    if highest_prime_factor == 1:
        highest_prime_factor = number

    return highest_prime_factor


if __name__ == '__main__':
    print(
        largest_prime_factor(
            number=600851475143
        )
    )
