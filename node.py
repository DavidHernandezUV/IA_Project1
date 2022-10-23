import numpy as np


class Node:

    def __init__(self, puzzle, father, operator, depth):
        self.puzzle = puzzle
        self.father = father
        self.operator = operator
        self.depth = depth
        self.ROWS = len(puzzle)
        self.COLS = len(puzzle[0])

    def move(self, direction):
        row = 0
        col = 0
        son = np.array(self.puzzle, copy=True)


puzzle = [[1, 2], [3, 4]]
node = Node(puzzle, 0, 0, 0)
node.move()
