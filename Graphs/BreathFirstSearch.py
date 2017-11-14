from DinamicArrayQueue import DinamicArrayQueue

def bfs(G,s):
    start = G.get_vertex(s)
    start.set_distance(0)
    start.set_previous(None)
    vertQueue = DinamicArrayQueue()
    vertQueue.enqueue(start)
    while not vertQueue.isEmptyQueue():
        currentVert=vertQueue.dequeue()
        print(currentVert.get_vertex_ID())
        for nbr in currentVert.get_connections():
            if nbr.visited == False:
                nbr.set_visited(True)
                nbr.set_distance(currentVert.get_distance()+1)
                nbr.set_previous(currentVert)
                vertQueue.enqueue(nbr)
            currentVert.set_visited(True)

def BFS_traversal(G):
    for v in G:
        if v.visited == False:
            bfs(G,v.get_vertex_ID())