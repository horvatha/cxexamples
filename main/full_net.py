#!/usr/bin/env python
# coding: utf-8
from __future__ import division
from __future__ import print_function
import igraph
import time

'''
Demonstration of the difference between adding edge one by one by one or all
at one time.

Author: Arpad Horvath
'''

def full_net(n=200):
    """Create a full network (graph).

    The edges are added one by one.
    """
    net = igraph.Graph(n)
    for i in range(n):
        for j in range(i):
            net.add_edge(i,j)
    ecount = net.ecount()
    assert n * (n - 1)/2  ==  ecount
    print("One by one: {0} edges created.".format(ecount))
    return net

def full_net2(n=200):
    """Create a full network (graph).

    Edges are added simultaneously.
    """
    pass


if __name__ == '__main__':
    print("Creating two full networks with 200 vertices.")
    start = time.time()
    net = full_net()
    stop1 = time.time()
    net = full_net2()
    stop2 = time.time()
    print("One by one:     {0:9.6f} s.\n"
          "Simultaneously: {1:9.6f} s.".format(
              stop1 - start,
              stop2 - stop1
              )
         )
