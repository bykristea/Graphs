from util import Stack, Queue  # These may come in handy

'''
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consits of 1s that are connected to the north, south, east, or west.
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
big_islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
               [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
               [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
               [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
               [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
               [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
               [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

  island_counter(islands) #returns 4
  '''
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
island_counter(islands)  # returns 4

# translate the problem into graphs terminology. Nodes would be 1's(also 0s). edges are when 1's are connected to the n, s, e, w. undirected graph because always two directions. is cyclic so need to keep track of visited nodes. Island is a connected component.
# build your graph: loop through the ilsands do a bfs. mark them as visited and add to counter.
# traverse your graph
# 2d Array is an array of an array.


def get_neighbors(vertex, graph_matrix):
    x = vertex[0]
    y = vertex[1]
    neighbors = []
    # check north
    if y > 0 and graph_matrix[y-1][x] == 1:
        neighbors.append((x, y-1))
    # check south
    if y < len(graph_matrix) - 1 and graph_matrix[y+1][x] == 1:
        neighbors.append((x, y+1))
    # check east
    if x < len(graph_matrix[0]) - 1 and graph_matrix[y][x+1] == 1:
        neighbors.append((x+1, y))
    # check west
     if x > 0 and graph_matrix[y][x-1] == 1:
        neighbors.append((x-1, y))
    return neighbors


def bft(x, y, matrix, visited):
    q = Queue
    q.enqueue((x, y))
    while q.size() > 0:
        v = q.dequeue()
        x = v[0]
        y = v[1]
        if v not in visited[y][x]:
            visited[y][x] = True
            for neighbor in get_neighbors((x, y), matrix):
                q.enqueue(neighbor)
    return visited


def island_counter(matrix):
    # loop through islands
    # do a bfs and count how many times that BFT occurs

    # create a visited matrix
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))

    # create a counter, initialize to 0
    counter = 0
    # walk through each cel in the original matrix
    for x in range(len(matrix[0])):  # row
        for y in range(len(matrix)):  # col

            # if it has not been visited. get row y then col x. always that order
            if not visited[y][x]:
                # if you reach 1
            if matrix[y][x] == 1:
                # do a BFT and march each 1 as visited
                visited = bft(x, y, matrix, visited)
                # increment counter by 1
                counter += 1
    return counter
