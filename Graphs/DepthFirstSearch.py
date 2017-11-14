from DinamicArrayQueue import DinamicArrayQueue

def dfs(G,currentVert,visited):
    visited[currentVert]=True
    print("traversal: " + currentVert.get_vertex_ID())
    for nbr in currentVert.get_connections():
        if nbr not in visited:
            dfs(G,nbr,visited)

def DFS_traversal(G):
    visited={}
    for currentVert in G:
        if currentVert not in visited:
            dfs(G,currentVert,visited)