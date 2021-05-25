test_maze = [[3,0,6,0,0,0],
             [1,9,1,1,1,0],
             [1,1,1,1,1,0],
             [1,1,1,1,1,0],
             [1,1,1,1,1,0],
             [1,1,1,1,1,0],
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

wrapped_maze = maze_wrapper(test_maze)

#print adjacent nodes- above, right, below, left
def show_adjacent(wrapped_maze, row_num, index_num):
    row_num+=1
    index_num+=1
    print("Above: ", wrapped_maze[row_num-1][index_num])
    print("Right: ", wrapped_maze[row_num][index_num+1])
    print("Below: ", wrapped_maze[row_num+1][index_num])
    print("Left: ", wrapped_maze[row_num][index_num-1])

show_adjacent(wrapped_maze, 0, 1)
    