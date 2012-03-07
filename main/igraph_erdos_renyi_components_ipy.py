# 2. hálózatos gyakorlathoz
# ipython -pylab után
# Lásd. halozatok_segedlet.tex

from igraph import Graph, summary
from igraph import plot as iplot
# iplot néven, hogy ne keveredjen a pylab.plot függvénnyel

# Programfájlban kellene még ez a sor is a -pylab opció helyett:
 from pylab import plot, average, array, grid, xlabel, ylabel, legend, show
# vagy egyszerűen
 from pylab import *
# és minden plot függvény után kellene
# show() függvény.
 import pylab
# esetén pedig pylab.függvény() alakban hívhatóak a pylab függvényei.

net = Graph.Erdos_Renyi(1000, .001)

summary(net)

M=net.ecount()
N = net.vcount()
Mmax = N*(N-1)/2
Mmax
M/Mmax
p = 1.*M/Mmax

net.diameter()

net.components()
cc=net.components()  # (összefüggő) komponensek, (connected) components
ccs = cc.sizes()
max(ccs)
average(ccs)
css   # Így kifut.
array(ccs)  # Így jobban néz ki, csak pylabbal vagy numpy-vel
len(ccs)   # ipython parancssorban a zárójel elhagyható
sizedist = [ccs.count(i) for i in range(max(ccs)+1)]
array(sizedist)
plot(sizedist, "o")
grid()
"A komponensek méreteloszlása".decode("utf-8")   # unicode sztring lesz.
title("A komponensek méretei".decode("utf-8"))
xlabel("")

title("A komponensek méretgyakorisága (Erdős-Rényi 1000,0.001)".decode("utf-8"))
xlabel("méret (csúcsok száma)".decode("utf-8"))
ylabel("darabszám".decode("utf-8"))
savefig("meretgyakorisag_ER1000_001.pdf")

len(cc)
cc_subgr = [cc.subgraph(i) for i in range(len(cc))]  # Az egyes komponensek, mint részgráfok.
delta = [sg.ecount() - sg.vcount() for sg in cc_subgr]
delta
array(delta)
max(delta)
# ha -1, akkor fa, ha 0, akkor egy kör van benne, különben több kör

gc = cc.giant()  # A legnagyobb (óriás) komponens, legtöbb csúcs
plot(gc)  # Ez így átláthatatlan.
plot(gc, layout="kk")
plot(gc, "giant_componentER1000_001.pdf", layout="kk") # Így elmenti.
from igraph import plot as iplot
# iplot néven, hogy ne keveredjen a pylab.plot függvénnyel
iplot(gc, layout="kk")
iplot(gc, "giant_componentER1000_001.pdf", layout="kk")

# Megnéztük egy kicsit más p-re is, és jelentősen mást kaptunk.
net = Graph.Erdos_Renyi(1000, .0015)
summary(net)
cc = net.components()
gc = cc.giant()
gc.vcount()
1000/275.
ccs = cc.sizes()
sizedist = [ccs.count(i) for i in range(max(ccs)+1)]
array(sizedist)
plot(sizedist[:20], "o")
array(ccs)
