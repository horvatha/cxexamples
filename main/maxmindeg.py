import igraph
class Network(igraph.Graph):
    def maxmindegree(self, write=True):
        "Returns with the maximal and minimal degree."
        deg = self.degree()
        if write:
            print("Maximal degree = {0}, "
                  "minimal degree = {1}".format(
                  max(deg),min(deg)))
        return max(deg), min(deg)

net = Network().Full(8)
maxd, mind = net.maxmindegree(write=False)
print(net.maxmindegree())
print(net.maxmindegree.__doc__)
