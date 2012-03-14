#!/usr/bin/env python
#coding: utf-8

"""

Authors:
 Czigány Zoltán
 Szabó Tamás
"""

#1.4 a feladat megoldása

def component(network, node):
    vizsgalt = []
    def magic(node_list):
        for i in node_list:
            if i not in vizsgalt:
                vizsgalt.append(i)
                magic(network.neighbors(i))
    magic([node])
    return vizsgalt

#1.4 b feladat megoldása

def delta(network, node_list):
    cc = network.subgraph(node_list)
    return cc.ecount() - cc.vcount()

if __name__ == "__main__":
    import igraph
    print "A feladat: A megadott csúcs-al rendelkezõ komponens összes csúcsának listája:"
    net = igraph.Graph(8, directed = False)
    net.add_edges([(0,1),(1,2),(2,3),(3,4),(3,5),(6,7)])
    node = 2
    comp = component(net, node)
    print comp
    print "B feladat: A megadott csúcsok alapján létrejött komponens éleinek számát kivonjuk a csúcsok számából:"
    #net2 = igraph.Graph.Erdos_Renyi(20,0.08)
    #nodes= [3,5,15,18,11,6]
    print delta(net, comp)
