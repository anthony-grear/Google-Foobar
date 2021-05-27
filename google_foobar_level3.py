test_maze = [[3,6,9,12,15,18],
             [1,1,1,1,1,21],
             [1,1,1,1,1,24],
             [1,1,1,1,1,27],
             [1,1,1,1,1,30],
             [1,1,1,1,1,33],
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

def get_adjacent(wrapped_maze, row_num, index_num):
    row_num+=1
    index_num+=1
    above = wrapped_maze[row_num-1][index_num]
    right = wrapped_maze[row_num][index_num+1]
    below = wrapped_maze[row_num+1][index_num]
    left = wrapped_maze[row_num][index_num-1]
    return (above, right, below, left)

print(get_adjacent(wrapped_maze, 0,1))

def touch_all_nodes(wrapped_maze):
    count1, count2 = 0, 0
    for row in wrapped_maze:
        for node in row:
            if node>1:
                print(node)
                print(wrapped_maze[count1-1][count2])
                print(wrapped_maze[count1][count2+1])
                print(wrapped_maze[count1+1][count2])
                print(wrapped_maze[count1][count2-1])
        count2 +=1
    count1 +=1

touch_all_nodes(wrapped_maze)

