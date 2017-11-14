import sys
from DinamicArrayQueue import DinamicArrayQueue

class Vertex:
    def __init__(self,node):
        self.id=node
        self.adjacent={}
        self.distance=0
        self.visited=False
        self.previous=None

    def add_neighbor(self,neighbor,weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_vertex_ID(self):
        return self.id

    def get_weight(self,node):
        return self.adjacent[node]

    def set_distance(self,dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self,prev):
        self.previous = prev

    def get_previous(self):
        return self.previous

    def set_visited(self,visited):
        self.visited=visited

    def get_visited(self):
        return self.visited

    def __str__(self):
        return str(self.id) + ' adjacent:' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vertDict={}
        self.numVertices=0

    def __len__(self):
        return self.numVertices

    def __iter__(self):
        return iter(self.vertDict.values())

    def add_vertex(self,node):
        self.numVertices +=1
        self.vertDict[node] = Vertex(node)

    def get_vertex(self,n):
        if n in self.vertDict:
            return self.vertDict[n]
        else:
            raise Exception("Vertex not found.")

    def add_edge(self,frm,to,cost=0):
        if frm not in self.vertDict:
            self.add_vertex(frm)
        if to not in self.vertDict:
            self.add_vertex(to)
        self.vertDict[frm].add_neighbor(self.vertDict[to],cost)
        # For directed graph don't add this.
        self.vertDict[to].add_neighbor(self.vertDict[frm],cost)

    def get_vertices(self):
        return self.vertDict.keys()

    def set_previous(self,current):
        self.previous = current

    def get_previous(self,current):
        return self.previous

    def get_edges(self):
        edges = []
        for v in self.vertDict.values():
            for w in v.get_connections():
                edges.append((v.get_vertex_ID(),w.get_vertex_ID(),v.get_weight(w)))
        return edges

    def reset_vertex(self):
        for vert in self.vertDict.values():
            vert.set_distance(-1)
            vert.set_previous(None)
            vert.set_visited(False)