#!/usr/bin/env python3.7

from math import floor
from typing import Tuple
from functools import reduce
from itertools import combinations_with_replacement


def factors(
    n: int      # Number to factorize
) -> Tuple[int]:
    return tuple(
        reduce(
            list.__add__,
            (
                [i, floor(n / i)]
                for i in range(1, int(n ** 0.5) + 1)
                if n % i == 0
            )
        )
    )


def all_pythagorean_triplets_of_n_dickson(
    n: int
) -> Tuple[Tuple[int]]:
    """
    https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples#Dickson's_method
    """
    n_2 = int(n ** 2 / 2)
    interesting_factors = factors(n_2)
    interesting_factors = tuple(
        combo
        for combo in combinations_with_replacement(interesting_factors, 2)
        if (combo[0] * combo[1]) == n_2
    )
    for s, t in interesting_factors:
        x, y, z = n + s, n + t, n + s + t
        if x + y + z == 1000:
            return x * y * z
    return 0


def find_pythagorean_triplet_whose_sum_match_n(
    n: int,
) -> int:
    max_value = int(n ** 1 / 3) + 1     # Cube root + 1 of n
    for x in range(6, max_value, 2):
        result = all_pythagorean_triplets_of_n_dickson(
            n=x
        )
        if result != 0 :
            return result


if __name__ == '__main__':
    print(
        find_pythagorean_triplet_whose_sum_match_n(1000)
    )
