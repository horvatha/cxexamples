#!/usr/bin/env python
# coding: utf-8

"""Creates the Prufer code.
"""

from __future__ import division
from __future__ import print_function
import igraph
import sys

__author__ = 'Paveszka Sándor'
# wh for def cl defs ifmain imp fr _ pdb + <Tab>
class Network(igraph.Graph):
    def prufer_code(self):
        """Returns with the Prufer code

        Returns
        -------
        With a Prufer code as a list of vertex names if
        the network is a tree, else with None.

        """
        net = self.copy()
        prufer_code = []
        vc = net.vcount()
        ec = net.ecount()
        if ec == vc -1 and net.is_connected():
            while net.vcount() > 2:
                leaf = net.degree().index(1)
                neig = net.neighbors(leaf)[0]
                name = int(net.vs[neig]["name"])
                prufer_code.append(name)
                net.delete_vertices(leaf)
            return prufer_code

def test():
    for  hdill in ["1--4--7, 2--5--8, 3--2--6",
            "1--2--3--4, 2--5, 3--6"]:
        testnet = Network.Formula(hdill)
        code = testnet.prufer_code()
        if code is None:
            print ("None")
        else:
            print (format(code))

if __name__ == "__main__":
    test()

