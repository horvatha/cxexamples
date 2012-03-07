# ipython -pylab után
# Lásd. halozatok_segedlet.tex

import igraph
g = igraph.Graph()
g.vcount()
g.ecount()
g.add_vertices?
g.add_vertices(5)
g.add_edges([(0,2), (2,5), (2,3), (5,4)])
igraph.plot(g)
igraph.plot(g, layout="circular")
g.vs["label"] = ["Hapci", "Morgó", "Tudor", "Vidor", "Kuka", "Szende"]
igraph.plot(g, layout="circular")
igraph.plot(g, layout="circular", margin=50)
g.delete_vertices(2)
igraph.plot(g, layout="circular", margin=50)


g = igraph.Graph(directed=True)
g.add_vertices(99)
for v in range(99):
    g.add_edges( (v, v+1) )
igraph.plot(g, layout="circular")
g.vcount(), g.ecount()

g = igraph.Graph(directed=True)
g.add_vertices(6)
li = range(7)
li.remove(4)
for i in li:
    g.add_edges((4,i))

g.successors(4)
g.predecessors(4)
g.neighbors(4, type=igraph.OUT) # Ugyanaz, mint a successors.
g.neighbors(4, type=igraph.IN) # Ugyanaz, mint a predecessors.

g.successors(0)
g.predecessors(0)
sg=g.subgraph([2,3,4])
N, M = sg.vcount(), sg.ecount()

with open("/home/ha/.bashrc") as f: # Csak olvasható
    lines =f.readlines()

line = lines[0]
line.split()

f=open("/home/ha/.bashrc", "w") # Csak írható
