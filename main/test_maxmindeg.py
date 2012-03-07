#!/usr/bin/env python
# coding: utf-8

"""Short unittest for maxmindeg.py."""

import maxmindeg
import unittest

class testNetwork(unittest.TestCase):
    def testDegree(self):
        "maxmindeg should return with (N-1, N-1) for full graphs"
        net = maxmindeg.Network.Full(8)
        maxd, mind = net.maxmindegree(write=False)
        self.assertEqual(maxd, 7)
        self.assertEqual(mind, 7)

if __name__ == "__main__":
    unittest.main()
