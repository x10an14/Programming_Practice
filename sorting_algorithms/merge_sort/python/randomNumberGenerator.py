#! python
import random

# From:
# http://bytes.com/topic/python/answers/829129-generate-random-list-integers


def random_ints(amount, lower=0, upper=100):
    return [random.randrange(lower, upper + 1) for i in range(amount)]

# print random_ints(100)
