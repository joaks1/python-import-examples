#! /usr/bin/env python3

"A module for getting the smallest prime factor of an integer."

import sys


# Note: this is not a very efficient way of doing this.
# How might you make this more efficient
def get_smallest_prime_factor(x):
    """
    Returns the smallest integer that is a factor of `x`.
    
    If `x` is a prime number `None` is returned.
    """
    for i in range(2, x):
        if (x % i) == 0:
            return i
    return None


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(sys.argv[0] + ": Expecting one command line argument -- the integer for which to get the smallest factor")
    n = int(sys.argv[1])
    if n < 1:
        sys.exit(sys.argv[0] + ": Expecting a positive integer")

    f = get_smallest_prime_factor(n)

    if f is None:
        print(n)
    else:
        print(f)
