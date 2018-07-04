#####################################################
#
# Coded by: Enrique B. Dutra
# In : 07/03/18
#
#####################################################

#[(vertice, edge, vertice)]


    def __init__(self):
        self.graph = []

    #insert a relation between graphs
    def insertRelation(self, x, y, z):
        relation = (x,y,z)
        self.graph.append(relation)
    #Transform a digraph into a undirected graph
    #def transformUnGraph(g):



