def path_finder(Matrix,position,N):
    if position == (N-1,N-1):
        return [(N-1,N-1)]
    x,y = position
    if x+1 < N and Matrix[x+1][y] == 1:
        a = path_finder(Matrix,(x+1,y),N)
        if a != None:
            return [(x,y)]+a
    if y+1<N and Matrix[x][y+1]==1:
        b = path_finder(Matrix,(x,y+1),N)
        if b != None:
            return[(x,y)]+b
Matrix = [[1,1,1,1,0],[0,1,0,1,0],[0,1,0,1,0],[0,1,0,0,0],[1,1,1,1,1]]
print path_finder(Matrix,(0,0),5)