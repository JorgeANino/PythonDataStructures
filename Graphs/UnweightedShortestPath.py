from DinamicArrayQueue import DinamicArrayQueue

def unweighted_shortest_path(G,s):
    source = G.get_vertex(s)
    source.set_distance(0)
    source.set_previous(None)
    q = DinamicArrayQueue()
    q.enqueue(source)
    while not q.isEmptyQueue():
        vert = q.dequeue()
        for nbr in vert.get_connections():
            if nbr.get_distance() == -1:
                nbr.set_distance(vert.get_distance()+1)
                nbr.set_previous(vert)
                q.enqueue(nbr)
    for v in G.vertDictionary.values():
        print(source.get_vertex_ID(), "to", v.get_vertex_ID(), "--->", v.get_distance())

