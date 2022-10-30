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

    # findPeople:
    # Find Mario's and Yoshi's positions in the gameboard

    def findPeople(self):
        coordinatesMatrix = np.nditer(self.state, flags=['multi_index'])
        for element in coordinatesMatrix:
            if element == self.MARIO:
                self.marioPos = coordinatesMatrix.multi_index
            if element == self.YOSHI:
                self.yoshiPos = coordinatesMatrix.multi_index

        print("MARIO ESTÁ EN: ", self.marioPos)
        print("YOSHI ESTÁ EN: ", self.yoshiPos)

    def avoidGoingBack(gameboard, sonGameboard, direction):
        pass
    # searchByAmplitude
    # Searchs by amplitude :D

    def searchByAmplitude(self):

        queue = []
        initialNode = node.Node(self.state, None, None, 0, 0, self.marioPos)
        queue.append(initialNode)

        while True:

            if len(queue) == 0:
                print("Falló, vas a perder IA")

            # currentNode is now initial node and queue becomes empty
            currentNode = queue.pop(0)

            # Checks if the position of Mario equals Yoshi's
            if currentNode.goalReached(self.yoshiPos):
                print("Voy a ganar IA")
                break

            # expand currentNode with the possible directions
            sonGameBoard, sonMarioPos = currentNode.move(self.LEFT)

            # Check if new node is different from the current node
            if not (np.array_equal(sonGameBoard, currentNode.getGameBoard())):
                # If the current node is not the initial, it has grandparents
                if (currentNode.getDepth() > 0):
                    # Check if the new node is different from the grandparent, TO AVOID GOING BACK
                    if not (np.array_equal(sonGameBoard, currentNode.getFather().getGameBoard())):
                        queue.append(node.Node(sonGameBoard, currentNode, self.LEFT,
                                               currentNode.getDepth()+1, currentNode.getCost()+1, sonMarioPos))
                # If the node is the initial node, the new node is added without checking if it can go back
                else:
                    queue.append(node.Node(sonGameBoard, currentNode, self.LEFT,
                                           currentNode.getDepth()+1, currentNode.getCost()+1, sonMarioPos))

            sonGameBoard, sonMarioPos = currentNode.move(self.DOWN)
            # Check if new node is different from the current node
            if not (np.array_equal(sonGameBoard, currentNode.getGameBoard())):
                # If the current node is not the initial, it has grandparents
                if (currentNode.getDepth() > 0):
                    if not (np.array_equal(sonGameBoard, currentNode.getFather().getGameBoard())):
                        queue.append(node.Node(sonGameBoard, currentNode, self.DOWN,
                                               currentNode.getDepth()+1, currentNode.getCost()+1, sonMarioPos))

                else:
                    queue.append(node.Node(sonGameBoard, currentNode, self.DOWN,
                                           currentNode.getDepth()+1, currentNode.getCost()+1, sonMarioPos))

            sonGameBoard, sonMarioPos = currentNode.move(self.RIGHT)
            # Check if new node is different from the current node
            if not (np.array_equal(sonGameBoard, currentNode.getGameBoard())):
                # If the current node is not the initial, it has grandparents
                if (currentNode.getDepth() > 0):
                    if not (np.array_equal(sonGameBoard, currentNode.getFather().getGameBoard())):
                        queue.append(node.Node(sonGameBoard, currentNode, self.RIGHT,
                                               currentNode.getDepth()+1, currentNode.getCost()+1, sonMarioPos))

                else:
                    queue.append(node.Node(sonGameBoard, currentNode, self.RIGHT,
                                           currentNode.getDepth()+1, currentNode.getCost()+1, sonMarioPos))

            sonGameBoard, sonMarioPos = currentNode.move(self.UP)
            # Check if new node is different from the current node
            if not (np.array_equal(sonGameBoard, currentNode.getGameBoard())):
                # If the current node is not the initial, it has grandparents
                if (currentNode.getDepth() > 0):
                    if not (np.array_equal(sonGameBoard, currentNode.getFather().getGameBoard())):
                        queue.append(node.Node(sonGameBoard, currentNode, self.UP,
                                               currentNode.getDepth()+1, currentNode.getCost()+1, sonMarioPos))

                else:
                    queue.append(node.Node(sonGameBoard, currentNode, self.UP,
                                           currentNode.getDepth()+1, currentNode.getCost()+1, sonMarioPos))

            print(list(map(lambda x: x.getMarioPos(), queue)))
            print("length of queue", len(queue))
            # for element in queue:
            #  print(element.getGameBoard())

        print(currentNode.getDepth())
