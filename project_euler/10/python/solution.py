#!/usr/bin/env python3.7

from itertools import compress, cycle, count, islice


def erat3():
    """Faster function completely stolen from S/O."""
    d = {9: 3, 25: 5}
    yield 2
    yield 3
    yield 5
    mask = 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
    modulos = frozenset((1, 7, 11, 13, 17, 19, 23, 29))

    for q in compress(
        islice(count(7), 0, None, 2),
        cycle(mask)
    ):
        p = d.pop(q, None)
        if p is None:
            d[q * q] = q
            yield q
        else:
            x = q + 2 * p
            while x in d or (x % 30) not in modulos:
                x += 2 * p
            d[x] = p


if __name__ == '__main__':
    prime_sum = 0
    for index, prime in enumerate(erat3()):
        # if index % 1_000 == 0:
        #     print(index, prime, prime_sum)
        if prime >= 2_000_000:
            break
        prime_sum += prime
    print(prime_sum)
