# cxnet.Graph   == igraph.Graph
# cxnet.plot    == igraph.plot
# cxnet.summary == igraph.summary
# IN, OUT, WEAK and STRONG are the same in cxnet as in igraph
# cxnet.Network derived from Graph
#     methods added: plot, cx*

# ipython -pylab

import cxnet
net = cxnet.debnetwork()
N = net.vcount()
M = net.ecount()
N, M
cxnet.summary(net)

##############################
#  Components
##############################
scc = net.components()
scc  # strongly connected components
sizes = scc.sizes()
len(sizes)
max(sizes)
giant = scc.giant()  # giant component
cxnet.plot(giant)
giant.plot()
net.cxneighbors("xserver-xorg")
net.cxneighborhood("xserver-xorg", plot=True)
net.cxneighborhood("vim", plot=True)
net.cxneighborhood("evince", plot=True)
net.cxneighborhood("python3", plot=True)
net.components?   # WEAK = 1, STRONG = 2
wcc = net.components(mode=1) #1: weakly c.c.
wcc = net.components(mode=cxnet.WEAK) # with the cxnet revision >330
wcc  # weakly connected components
sizes = wcc.sizes()
len(sizes)
array(sizes)
net.diameter?
%time net.diameter(directed=False)
M,N
2.*M/N
deg = net.degree()
net.cxneighborhood("evince", plot=True)

##############################
#  Degrees
##############################
max(deg)
for v in net.vs:
    if net.degree(v) == max(deg):
        print v["name"]

dd = [deg.count(k) for k in range(max(deg)+1)]
dd[:10]
plot(d[:20])
plot(dd[:20])
plot(dd)
loglog(dd)
loglog(dd, "o")
N=float(N)
dd = [d/N for d in dd]
dd[:10]  # degree distribution, 0..9 degrees
