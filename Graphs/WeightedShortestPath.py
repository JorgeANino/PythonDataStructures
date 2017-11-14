from AdjListGraph import Graph,Vertex
from DinamicArrayQueue import DinamicArrayQueue
import heapq
"""
Incorrect implementation of Djikstras
"""


def djikstra(G,s):
    source = G.get_vertex(s)
    source.set_distance(0)
    unvisitedQueue = [(v.get_distance(),v) for v in G.vertDict.values()]
    heapq.heapify(unvisitedQueue)
    while len(unvisitedQueue):
        uv = heapq.heappop(unvisitedQueue)
        current = uv[1]
        current.set_visited(True)
        for next in current.adjacent.keys():
            if next.visited:
                continue
            newDist = current.get_distance() + current.get_weight(next)
            next.set_distance(newDist)
            print("Updated : current = %s next = %s newDist = %s" % (current.get_vertex_ID(), next.get_vertex_ID()
                                                                     , next.get_distance()))
            """
            if newDist > next.get_distance():
                next.set_distance(newDist)
                next.set_previous(current)
                print("Updated : current = %s next = %s newDist = %s" %(current.get_vertex_ID(),next.get_vertex_ID()
                                                                        ,next.get_distance()))
            else:
                print("Not updated: current = %s next = %s newDist = %s" %(current.get_vertex_ID(),next.get_vertex_ID()
                                                                           ,next.get_distance()))
            """
        while len(unvisitedQueue):
            heapq.heappop(unvisitedQueue)
        unvisitedQueue = [(v.get_distance(),v) for v in G.vertDict.values() if not v.visited]
        heapq.heapify(unvisitedQueue)





G = Graph()
G.add_vertex("a")
G.add_vertex("b")
G.add_vertex("c")
G.add_vertex("d")
G.add_vertex("e")
G.add_edge("a","b",40)
G.add_edge("a","c",60)
G.add_edge("c","b",30)
G.add_edge("b","e",20)
G.add_edge("c","d",10)
G.add_edge("d","e",15)
djikstra(G,"a")