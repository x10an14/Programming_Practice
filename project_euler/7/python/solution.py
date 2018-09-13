#!/usr/bin/env python3.7

from contextlib import suppress
from itertools import compress, cycle, count, islice

def erat3():
    """Faster function completely stolen from S/O."""
    D = {9: 3, 25: 5}
    yield 2
    yield 3
    yield 5
    MASK = 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
    MODULOS = frozenset((1, 7, 11, 13, 17, 19, 23, 29))

    for q in compress(
        islice(count(7), 0, None, 2),
        cycle(MASK)
    ):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = q
            yield q
        else:
            x = q + 2 * p
            while x in D or (x % 30) not in MODULOS:
                x += 2 * p
            D[x] = p


def generate_nth_prime_number(
    nth_prime: int
) -> int:
    """
    Prime number generator library function.
    Input: Anything.
    Output (if `nth_prime` can be cast into a positive integer): The generator will yield all
      primes up and including the `nth_prime`.
    Will raise TypeError if `nth_prime` cannot be cast into a positive integer.
    """
    with suppress(TypeError):
        nth_prime = int(nth_prime)
    if not type(nth_prime) is int or nth_prime < 0:
        raise TypeError("Input needs to be of positive integer type!")

    nth_prime -= 1  # For indexing correctness
    return next(islice(erat3(), nth_prime, nth_prime + 1))


if __name__ == '__main__':
    print(
        generate_nth_prime_number(
            nth_prime=10_001
        )
    )
