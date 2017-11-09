class Vertex:
    def __init__(self,node):
        self.id = node
        self.visited = False

    def add_neighbor(self,neighbor,G):
        G.add_edge(self.id,neighbor)

    def get_connections(self,G):
        return G.adjMatrix[self.id]

    def get_vertex_ID(self):
        return self.id

    def set_vertex_ID(self,id):
        self.id = id

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id)


class Graph:
    def __init__(self,numVertices,cost=0):
        self.adjMatrix=[[-1]*numVertices for _ in range(numVertices)]
        self.numVertices = numVertices
        self.vertices = []
        for i in range(self.numVertices):
            self.vertices.append(Vertex(i))

    def set_vertices(self,vtx,id):
        if vtx<0 or vtx>self.numVertices:
            raise Exception("Vertex index unvalid.")
        self.vertices[vtx].set_vertex_ID(id)

    def get_vertices(self,n):
        for i in range(0,self.numVertices):
            if n == self.vertices[i].get_vertex_ID():
                return i
        return -1

    def add_edge(self,frm,to,cost=0):
        if self.get_vertices(frm) != -1 and self.get_vertices(to) != -1:
            self.adjMatrix[self.get_vertices(frm)][self.get_vertices(to)] = cost
            # For directed graph don't add this.
            self.adjMatrix[self.get_vertices(to)][self.get_vertices(frm)] = cost

    def get_vertices_ids(self):
        vertices = []
        for i in self.vertices:
            vertices.append(i.get_vertex_ID())
        return vertices

    def print_matrix(self):
        for u in self.adjMatrix:
            print u

    def get_edges(self):
        edges = []
        for v in range(0,self.numVertices):
            for u in range(0,self.numVertices):
                edges.append((self.vertices[v].get_vertex_ID(),self.vertices[u].get_vertex_ID(),self.adjMatrix[v][u]))
        return edges


g = Graph(5)
g.set_vertices(0,"a")
g.set_vertices(1,"b")
g.set_vertices(2,"c")
g.set_vertices(3,"d")
g.set_vertices(4,"e")
g.add_edge("a","e",10)
g.add_edge("a","c",20)
g.add_edge("c","b",30)
g.add_edge("b","e",40)
g.add_edge("e","d",50)
g.add_edge("f","e",60)
g.print_matrix()
print g.get_edges()





