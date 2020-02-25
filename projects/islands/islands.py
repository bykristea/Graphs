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

# nodes: 1's
# edges: N.S.E.W neighbors not diagonals
# connected components: islands

# iterate through the matrix, if it's a 1 then we run DFT/BFT. mark everything we have visited.


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def getNeighbors(matrix, node):
    row = node[0]
    col = node[1]

    neighboring_islands = []
    stepNorth = stepSouth = stepWest = stepEast = False

    if row > 0:
        stepNorth = row - 1
    if col > 0:
        stepWest = col - 1
    if row < len(matrix) - 1:
        stepSouth = row + 1
    if col < len(matrix) - 1:
        stepEast = col + 1

    if stepNorth is not False and matrix[stepNorth][col] == 1:
        neighboring_islands.append((stepNorth, col))

    if stepSouth is not False and matrix[stepSouth][col] == 1:
        neighboring_islands.append((stepSouth, col))

    if stepWest is not False and matrix[row][stepWest] == 1:
        neighboring_islands.append((row, stepWest))

    if stepEast is not False and matrix[row][stepEast] == 1:
        neighboring_islands.append((row, stepEast))


def dft(matrix, node, visited):
    stack = Stack()
    stack.push(node)
    while stack.size() > 0:
        current_node = stack.pop()

        if node not in visited:
            visited.add(node)
            neighbors = getNeighbors(matrix, node)
            for neighbor in neighbors:
                stack.push(neighbor)


def islands_counter(matrix):
    total_islands = 0
    visited = set()
    # iterate through the matrix
    # if its a 1 then we run DFT/BFT
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            node = (row, col)
            if node not in visited and matrix[row][col] == 1:
                visited.add(node)
                dft(matrix, node, visited)
                total_islands += 1

    return total_islands
