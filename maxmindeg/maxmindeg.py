#!/usr/bin/env python
# coding: utf-8

"""Docstring of the module maxmindeg
"""

from __future__ import division
from __future__ import print_function
import igraph

__author__ = 'Arpad Horvath'
# wh for def cl defs ifmain imp fr _ pdb + <Tab>

class Network(igraph.Graph):
    def maxmindegree(self):
        deg = self.degree()
        return max(deg), min(deg)
    def component(self, vertex):
        vlist = [vertex]
        while True:
            nlist = [self.neighbors(v) for v in vlist]
            for n in nlist:
                vlist.extend(n)
            newneighbors = False
            for v in vlist:
                for n in self.neighbors(v):
                    if not (n in vlist):
                        newneighbors = True
            if not newneighbors:
                break
        return list(set(vlist))

