#! /usr/bin/env python3

"A module for factoring integers."

import sys
import smallest_factor


# Note: this is not a very efficient way of doing this.
# How might you make this more efficient
def factor_into_primes(x):
    "Returns a list of prime numbers that are factors of `x`."
    current_x = x
    primes = []
    while True:
        y = smallest_factor.get_smallest_prime_factor(current_x)
        if y is None:
            break
        primes.append(y)
        current_x = current_x // y
    primes.append(current_x)
    return primes


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(sys.argv[0] + ": Expecting one command line argument -- the integer to factor into primes")
    n = int(sys.argv[1])
    if n < 1:
        sys.exit(sys.argv[0] + ": Expecting a positive integer")

    primes = factor_into_primes(n)
    
    primes_as_strings = []
    product = 1
    for p in primes:
        primes_as_strings.append(str(p))
        product = product * p
    
    assert product == n
    
    print(" ".join(primes_as_strings))
