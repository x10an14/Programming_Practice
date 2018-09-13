#!/usr/bin/env python3.7


def difference_between_sum_of_squares_and_sum_of_n_first_natural_numbers(n: int) -> int:
    """
    Difference between A and B^2, given that:

    Sum of all natural numbers up to n:
    B = n*(n + 1)/2

    Sum of the squares of all natural numbers up to n:
    A = n(n + 1)(2n + 1)/6
    """

    A = n * (n + 1) * ((2 * n) + 1) / 6
    B = n * (n + 1) / 2
    B_squared = B ** 2
    return int(abs(A - B_squared))


if __name__ == '__main__':
    print(
        difference_between_sum_of_squares_and_sum_of_n_first_natural_numbers(
            n=100
        )
    )
