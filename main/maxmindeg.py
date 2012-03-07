#!/usr/bin/env python
# coding: utf-8

"""Network is an inherited class of igraph.Graph.

It has one additional method: maxmindegree.

"""


import igraph
class Network(igraph.Graph):
    def maxmindegree(self, write=True):
        "Returns with the maximal and minimal degree."
        deg = self.degree()
        if write:
            print("Maximal degree = {0}, "
                  "minimal degree = {1}".format(
                  max(deg),min(deg)))
        return max(deg), min(deg)

if __name__ == '__main__':
    net = Network.Full(8)
    maxd, mind = net.maxmindegree(write=False)
    print(net.maxmindegree())
    print(net.maxmindegree.__doc__)
    net = Network.Formula("a-b-c-d, a-c, b-d")
    print(net.maxmindegree(False))
