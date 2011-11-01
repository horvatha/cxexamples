# 1. hálózatos gyakorlathoz
# ipython -pylab után
# Lásd. halozatok_segedlet.tex

import igraph
gr = igraph.Graph()
gr.vcount()
gr.ecount()
gr.add_vertices?
gr.add_vertices(5)
gr.add_edges([(0,2), (2,5), (2,3), (5,4)])
igraph.plot(gr)
igraph.plot(gr, layout="circular")
gr.vs["label"] = ["Hapci", "Morgó", "Tudor", "Vidor", "Kuka", "Szende"]
igraph.plot(gr, layout="circular")
igraph.plot(gr, layout="circular", margin=50)
gr.delete_vertices(2)
igraph.plot(gr, layout="circular", margin=50)


gr = igraph.Graph(directed=True)
gr.add_vertices(99)
for v in range(99):
    gr.add_edges( (v, v+1) )
igraph.plot(gr, layout="circular")
gr.vcount(), gr.ecount()

gr = igraph.Graph(directed=True)
gr.add_vertices(6)
li = range(7)
li.remove(4)
for i in li:
    gr.add_edges((4,i))

gr.successors(4)
gr.predecessors(4)
gr.neighbors(4, type=igraph.OUT) # Ugyanaz, mint a successors.
gr.neighbors(4, type=igraph.IN) # Ugyanaz, mint a predecessors.

gr.successors(0)
gr.predecessors(0)
sg=gr.subgraph([2,3,4])
N, M = sg.vcount(), sg.ecount()

f=open("/home/ha/.bashrc") # Csak olvasható
lines =f.readlines()
for line in lines:
    a, b = line.split()

f=open("/home/ha/.bashrc", "w") # Csak írható
