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

    def showDepth(self):
        print("La profundidad del nodo es:", self.depth)

    def showOperator(self):
        print("El operador usado fue:", self.operator)

    def showPuzzle(self):
        print(self.puzzle)


puzzle = [[1, 2], [3, 4]]
node = Node(puzzle, 0, 'izquierda', 2)
node.move(2)
node.showDepth()
node.showOperator()
node.showPuzzle()
