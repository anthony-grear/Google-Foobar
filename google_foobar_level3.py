test_maze = [[0,1,1,0,0,0],
             [0,0,0,0,1,1],
             [0,1,1,1,1,0],
             [0,1,1,1,1,0],
             [0,1,1,1,1,0],
             [0,1,1,1,1,0],
            ]

def maze_wrapper(maze):
    maze_dimension = len(maze[0])
    maze_border = [-1]*(maze_dimension+2)
    for maze_row in maze:
        maze_row.insert(0,-1)
        maze_row.append(-1)
    
    maze.insert(0,maze_border)
    maze.append(maze_border)
    return maze 

for x in maze_wrapper(test_maze):
    print(x)