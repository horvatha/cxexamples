#!/usr/bin/env python
# coding: utf-8

'''
Creates the Prüfer code of a tree.

Author: Róth Bálint
License: GNU General Public License (GPL) 3 or newer
'''

import igraph
import sys


class MyGraph(igraph.Graph):

    def prufer(self):
        l = []
        N = self.vcount()
        M = self.ecount()
        if M == N - 1 and self.is_connected():
            while self.vcount() > 2:
                leaf = self.degree().index(1)
                n = self.neighbors(leaf)[0]
                name = int(self.vs[n]["name"])
                l.append(name)
                self.delete_vertices(leaf)
            return l
        else:
            return None

def test():
    for formula in ["1-2-3-4, 2-5, 3-6",
                    "1-2-3-1, 2-5, 3-6"]:
        testnet = MyGraph.Formula(formula)
        net = testnet.copy()
        code =  testnet.prufer()
        print 'Graph.Formula("{0}")'.format(formula)
        if code is None:
            print "Not tree."
        else:
            print  "Code of the tree: {}".format(code)

    #igraph.plot(net, vertex_label=range(1, net.vcount() + 1))

if __name__ == "__main__":
    test()
