#!/usr/bin/env python3.7


def is_evenly_divisble_up_to_20(n: int) -> bool:
    # Primes to consider
    # for x in (3, 5, 7, 11, 13, 17, 19):
    for x in range(3, 21):
        if n % x != 0:
            return False
    return True


if __name__ == '__main__':

    # n => product of primes to consider + 1
    n = 4_849_846
    while not is_evenly_divisble_up_to_20(n):
        n += 2
    print(n)
