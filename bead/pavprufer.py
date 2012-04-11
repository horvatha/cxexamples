#!/usr/bin/env python
# coding: utf-8

"""Docstring of the module beadando
"""

from __future__ import division
from __future__ import print_function
import igraph
import sys

__author__ = 'Paveszka Sándor'
# wh for def cl defs ifmain imp fr _ pdb + <Tab>
class Network(igraph.Graph):
    def coode(self):
        li = []
        vc = self.vcount()
        ec = self.ecount()
        if ec == vc -1 and self.is_connected():
            while vc > 2:
                level = self.degree().index(1)
                neig = self.neighbors(level)[0]
                name = int(self.vs[neig]["name"])
                li.append(name)
                self.delete_vertices(level)
                vc -= 1
            return li
        else:
            return None

def test():
    for  hdill in ["1--4--7, 2--5--8, 3--2--6",
            "1--2--3--4, 2--5, 3--6"]:
        testnet = Network.Formula(hdill)
        net = testnet.copy()
        code = testnet.coode()
        if code is None:
            print ("None")
        else:
            print (format(code))

if __name__ == "__main__":
    test()
