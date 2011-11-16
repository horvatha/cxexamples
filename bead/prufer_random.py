#!/usr/bin/env python
# coding: utf-8

import igraph

'''
Author: Vámos István
'''

def pruf(net):
    """Prüfer-kód létrehozása fából."""
    N=net.vcount()
    elek=net.get_edgelist()
    fokszam=[]
    for i in range(N):
        fokszam.append(net.degree(i))
    prufer=[]
    i=0
    while i<N:
        if fokszam.__getitem__(i)==1:
            for j in range(N-1):
                Q,W=elek.__getitem__(j)
                if Q==i:
                    prufer.append(W)
                    temp=fokszam.__getitem__(W)
                    fokszam.__setitem__(W,temp-1)
                    elek.pop(j)
                    i=0
                    fokszam.__setitem__(Q,0)
                    break
                if W==i:
                    prufer.append(Q)
                    temp=fokszam.__getitem__(Q)
                    fokszam.__setitem__(Q,temp-1)
                    elek.pop(j)
                    i=0
                    fokszam.__setitem__(W,0)
                    break
        else:
            i+=1
    return prufer[:-1]

def general(N):
    net=igraph.Graph.Erdos_Renyi(N,0.25)
    net.vs["label"] = range(N)
    return net

def vizsgalat(net):
    N=net.vcount()
    igraph.summary(net)
    cc=net.components()
    comp=len(cc.sizes())
    elek=net.ecount()
    if comp == 1 and elek == N-1:
        kod = pruf(net)
        print "Ez egy fa!"
    else:
        kod = None
    print kod
    print ""
    print ""
    return kod

def generator(N):
    fa=None
    while fa==None:
        net=general(N)
        fa=vizsgalat(net)
    igraph.plot(net)
    return fa

if __name__=="__main__":
    import sys
    generator(int(sys.argv[1]))

