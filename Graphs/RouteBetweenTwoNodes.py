from AdjListGraph import Graph
from DinamicArrayQueue import DinamicArrayQueue

def path_between(G,frm,to):
    source = G.get_vertex(frm)
    q = DinamicArrayQueue()
    q.enqueue(source)
    while not q.isEmptyQueue():
        vert = q.dequeue()
        for nbr in vert.get_connections():
            if nbr == G.vertDict[to]:
                return True
            if nbr.visited == False:
                nbr.set_visited(True)
                q.enqueue(nbr)
            vert.set_visited(True)
    return False

G = Graph()
G.add_vertex("a")
G.add_vertex("b")
G.add_vertex("c")
G.add_vertex("d")
G.add_vertex("e")
G.add_edge("a","b",4)
G.add_edge("a","c",1)
G.add_edge("c","b",2)
G.add_edge("b","e",4)
G.add_edge("c","d",4)
G.add_edge("d","e",4)
print(G.get_edges())
print(path_between(G,"a","d"))



