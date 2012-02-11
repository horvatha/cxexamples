##!/usr/bin/env python
# coding: utf-8

"""Tests of the prim module
"""

from __future__ import division
from __future__ import print_function
import unittest
import prime

__author__ = 'Arpad Horvath'
# cl wh for ifmain def defs imp

#Eratosthenes' sieves = Eratoszthenészi szita

# test for success
class TestKnownValues(unittest.TestCase):
    known_values = [
        # maxi, prims, twin_prims
        (3,  [2,3], []),
        (20, [2,3,5,7,11,13,17,19],
             [(3,5), (5,7), (11,13), (17,19)]),
        ]

    p = prime.Primes(maxi=20)

    def test_known_values(self):
        "prims and twin prims should be as in the known values"
        for maxi, primes, twin_primes in self.known_values:
            p = prime.Primes(maxi=maxi)
            self.assertEqual(p.primes, primes)
            self.assertEqual(p.twin_primes(), twin_primes)

    def test_prims(self):
        "isprime should give the proper boolean value"
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        not_primes = [i for i in range(1,21) if i not in primes]
        for i in primes:
            self.assertTrue(self.p.isprime(i))
        for i in not_primes:
            self.assertFalse(self.p.isprime(i))

# test for failure
class TestBadValues(unittest.TestCase):
    p = prime.Primes(maxi=20)

    def test_bad_maxi(self):
        "__init__ should fail with not integer and < 2 values."
        for maxi in [-3, 5.5, 4.0, 0, 1]:
            self.assertRaises(AssertionError, prime.Primes, maxi)

    def test_bad_twin_prime_value(self):
        "twin_primes should fail with not integer and too big or small values."
        for n in [-3, 5.5, 4.0, 0, 1, 2, 21]:
            self.assertRaises(AssertionError, self.p.isprime, n)


if __name__ == '__main__':
    unittest.main()

