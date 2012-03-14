#!/usr/bin/env python
# coding: utf-8

"""Docstring of the module mmd
"""

from __future__ import division
from __future__ import print_function

# wh for def cl defs ifmain imp fr _ pdb + <Tab>

"""Kiírja a maximális és minimális fokszámot.
"""

import maxmindeg
import igraph

net = maxmindeg.Network.Formula("a-b-c,d-b-e,f-g,h")
for v in net.vs:
    print(v.index, v["name"])
print(net.vs["name"])
print(net.component(0))
# print(net.maxmindegree())
igraph.plot(net)


