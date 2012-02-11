##!/usr/bin/env python
# coding: utf-8

"""Lists primes and twin primes.
"""

from __future__ import division
from __future__ import print_function

__author__ = 'Arpad Horvath'
# cl wh for ifmain def defs imp

class Primes(object):
    """Create the list of primes.
    """
    def __init__(self, maxi=10000):
        assert isinstance(maxi, int) and maxi > 1
        self.maxi = maxi
        nums = range(maxi+1)
        nums[0:2] = [0, 0]
        for i in range(2, maxi+1):
            if nums[i] != 0:
                j = 2*i
                while j <= maxi:
                    nums[j] = 0
                    j += i
        self.primes = [p for p in nums if p != 0]

    def twin_primes(self):
        return [(self.primes[i], self.primes[i+1])
                for i in range(len(self.primes) - 1)
                if self.primes[i] + 2 == self.primes[i+1]
            ]

    def isprime(self, n):
        assert isinstance(n, int) and 0 < n <= self.maxi
        return n in self.primes



