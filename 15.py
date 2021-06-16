maxgridsize = 20

def lattice_paths_count(size):
    #create empty grid of gridsize
    grid = [[None for i in range(size)] for j in range(size)]

    #loop through all blocks
    for y in reversed(range(size)):
        for x in reversed(range(size)):
            #last block
            if(x == size-1 and y == size-1):
                grid[x][y] = 2
            #bottom row
            elif(x == size-1):
                grid[x][y] = grid[x][y+1] + 1
            #right column
            elif(y == size-1):
                grid[x][y] = grid[x+1][y] + 1
            #everything else
            else:
                grid[x][y] = grid[x+1][y] + grid[x][y+1]

    #loop through rows
    for y in grid:
        row = ""
        #loop through columns
        for x in y:
            row += str(x) + "\t"
    
    return(grid[0][0])
    
for i in range(1, maxgridsize+1):
    print(lattice_paths_count(i))
    print("")