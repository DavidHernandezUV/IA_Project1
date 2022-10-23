import numpy as np
import node


class GameBoard:
    # CONSTANTS
    LEFT = 0
    DOWN = 1
    RIGHT = 2
    UP = 3
    EMPTY = 0
    BLOCK = 1
    MARIO = 2
    STAR = 3
    FLOWER = 4
    KOOPA = 5
    YOSHI = 6

    def __init__(self, state):
        self.state = state
        self.marioPos = [0, 0]
        self.yoshiPos = [0, 0]
    # Where is Mario

    def findPeople(self):
        coordinatesMatrix = np.nditer(self.state, flags=['multi_index'])
        for element in coordinatesMatrix:
            if element == self.MARIO:
                self.marioPos = coordinatesMatrix.multi_index
            if element == self.YOSHI:
                self.yoshiPos = coordinatesMatrix.multi_index

        print("MARIO ESTÁ EN: ", self.marioPos)
        print("YOSHI ESTÁ EN: ", self.yoshiPos)

    def searchByAmplitude(self):

        queue = []
        initialNode = node.Node(self.state, None, None, 1, 0, self.marioPos)
        queue.append(initialNode)

        i = 0
        while i < 1:
            if len(queue) == 0:
                print("Falló, vas a perder IA")
            currentNode = queue.pop(0)
            if currentNode.goalReached(self.yoshiPos):
                print("Voy a ganar IA")
            # expandir currentNode y meter hijos
            sonGameBoard, sonMarioPos = currentNode.move(self.LEFT)
            if (sonGameBoard == currentNode.getGameBoard()).all():
                queue.append(node.Node(sonGameBoard, currentNode, self.LEFT,
                                       currentNode.getDepth()+1, currentNode.getCost()+1, sonMarioPos))

            sonGameBoard, sonMarioPos = currentNode.move(self.DOWN)
            if (sonGameBoard == currentNode.getGameBoard()).all():
                queue.append(node.Node(sonGameBoard, currentNode, self.DOWN,
                                       currentNode.getDepth()+1, currentNode.getCost()+1, sonMarioPos))

            sonGameBoard, sonMarioPos = currentNode.move(self.RIGHT)
            if (sonGameBoard == currentNode.getGameBoard()).all():
                queue.append(node.Node(sonGameBoard, currentNode, self.RIGHT,
                                       currentNode.getDepth()+1, currentNode.getCost()+1, sonMarioPos))

            sonGameBoard, sonMarioPos = currentNode.move(self.UP)
            if (sonGameBoard == currentNode.getGameBoard()).all():
                queue.append(node.Node(sonGameBoard, currentNode, self.UP,
                                       currentNode.getDepth()+1, currentNode.getCost()+1, sonMarioPos))

            i = i+1
            print("length of queue", len(queue))
            for element in queue:
                print(element.getGameBoard())
