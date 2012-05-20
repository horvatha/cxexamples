#!/usr/bin/env python
# coding: utf-8

"""
Changing of the diameter of graph from the Barabasi Albert model
as the function of m.
"""

from __future__ import division
from __future__ import print_function

__author__ = 'Mencigár Richárd featuring Paveszka Sándor'

import igraph
import sys
import pylab
import time

def BA_ER_diameter(N,m):
    net=igraph.Graph.Barabasi(N,m)
    M=net.ecount()
    print("Number of edges M =", M, "m =", m)
    M_max=N*(N-1)/2
    p=M/M_max
    neterdos=igraph.Graph.Erdos_Renyi(N,p)
    return net.diameter(), neterdos.diameter()

def BA_ER_diam(N, m_max):
    BA_lista = []
    ER_lista = []
    for m in range(1, m_max+1):
        dBA, dER = BA_ER_diameter(N, m)
        BA_lista.append(dBA)
        ER_lista.append(dER)
    return BA_lista, ER_lista

def BA_ER_diam_plot(N, m_max):
    BA_lista, ER_lista = BA_ER_diam(N, m_max)
    pylab.plot(range(1, m_max+1), BA_lista, ".", label="BA")
    pylab.plot(range(1, m_max+1), ER_lista, "x", label="ER")
    pylab.legend()
    pylab.xlabel("m")
    pylab.ylabel("diameter")
    pylab.title("The diameter of the BA-graph and an equivalent random graph")
    pylab.savefig("BA_ER_diam.pdf")
    pylab.show()

def test():
    print(BA_ER_diam(N=1000, m_max=10))
    print(BA_ER_diameter(N=1000, m=3))

if __name__ == "__main__":
    BA_ER_diam_plot(1000, 20)
    #test()
    sys.exit(0)
