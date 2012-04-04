#!/usr/bin/env python
# coding: utf-8

"""Docstring of the module 3.3
"""

from __future__ import division
from __future__ import print_function

__author__ = 'Nagy Ádám, PRRICI'
# wh for def cl defs ifmain imp fr _ pdb + <Tab>
from pylab import *
import igraph

def ERN():
    p=linspace(0, 0.1, 100)
#felesleges 1-ig vizsgálni a valószínűséget, mert 0.1 felett csak 1 komponenst kapunk
    N=100
    comp=[]
    for i in p:
        net= igraph.Graph.Erdos_Renyi(N, i)
        cc=net.components()
        sizes=cc.sizes()
        cn=len(sizes)
        comp.append(cn)
    plot(p, comp)

