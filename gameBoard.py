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

    # Costs
    KOOPA_COST = 5
    MOVE_COST = 1
    MOVE_WITH_STAR_COST = 0.5

    # Powerups
    flowers_acum = 0
    star_effect = 0

    def __init__(self, state):
        self.state = state
        self.marioPos = [0, 0]
        self.yoshiPos = [0, 0]
        self.starsPos = []
        self.flowersPos = []
        self.koopasPos = []
        self.solution = []

    # findPeople:
    # Find Mario's and Yoshi's positions in the gameboard

    def findPeople(self):
        coordinatesMatrix = np.nditer(self.state, flags=['multi_index'])
        for element in coordinatesMatrix:
            if element == self.MARIO:
                self.marioPos = coordinatesMatrix.multi_index
            if element == self.YOSHI:
                self.yoshiPos = coordinatesMatrix.multi_index
            if element == self.KOOPA:
                self.koopasPos.append(coordinatesMatrix.multi_index)
            if element == self.FLOWER:
                self.flowersPos.append(coordinatesMatrix.multi_index)
            if element == self.STAR:
                self.starsPos.append(coordinatesMatrix.multi_index)

        print("MARIO ESTÁ EN: ", self.marioPos)
        print("YOSHI ESTÁ EN: ", self.yoshiPos)
        print("KOOPAS ESTÁN EN: ", self.koopasPos)
        print("FLOWERS ESTÁN EN: ", self.flowersPos)
        print("STAR ESTÁN EN: ", self.starsPos)

    # avoidGoingback: Node, array, matrix, tuple, number
    # Checks if the son is different from the grandparent, so that it avoids going back

    def avoidGoingBack(self, currentNode, queue, sonGameBoard, sonMarioPos, direction):
        # If the current node is not the initial, it has grandparents
        if (currentNode.getDepth() > 0):
            # Check if the new node is different from the grandparent, TO AVOID GOING BACK
            if not (np.array_equal(sonGameBoard, currentNode.getFather().getGameBoard())):
                queue.append(node.Node(sonGameBoard, currentNode, direction,
                                       currentNode.getDepth()+1, sonMarioPos))
        # If the node is the initial node, the new node is added without checking if it can go back
        else:
            queue.append(node.Node(sonGameBoard, currentNode, direction,
                                   currentNode.getDepth()+1, sonMarioPos))

    # searchByAmplitude
    # Searchs by amplitude :D

    def searchByAmplitude(self):

        queue = []
        initialNode = node.Node(self.state, None, None, 0, self.marioPos)
        print("initialNodeCost: ", initialNode.getCost())
        queue.append(initialNode)

        while True:

            if len(queue) == 0:
                print("Falló, vas a perder IA")

            # currentNode is now initial node and queue becomes empty
            currentNode = queue.pop(0)
            # Checks if the position of Mario equals Yoshi's
            if currentNode.goalReached(self.yoshiPos):

                print("Voy a ganar IA")
                self.findSolution(currentNode)
                break

            # expand currentNode with the possible directions
            sonGameBoard, sonMarioPos = currentNode.move(self.LEFT)
            # Check if new node is different from the current node
            if not (np.array_equal(sonGameBoard, currentNode.getGameBoard())):
                self.avoidGoingBack(currentNode, queue,
                                    sonGameBoard, sonMarioPos, self.LEFT)

            sonGameBoard, sonMarioPos = currentNode.move(
                self.DOWN)
            # Check if new node is different from the current node
            if not (np.array_equal(sonGameBoard, currentNode.getGameBoard())):
                self.avoidGoingBack(currentNode, queue,
                                    sonGameBoard, sonMarioPos, self.DOWN)

            sonGameBoard, sonMarioPos = currentNode.move(
                self.RIGHT)
            # Check if new node is different from the current node
            if not (np.array_equal(sonGameBoard, currentNode.getGameBoard())):
                self.avoidGoingBack(currentNode, queue,
                                    sonGameBoard, sonMarioPos, self.RIGHT)

            sonGameBoard, sonMarioPos = currentNode.move(
                self.UP)
            # Check if new node is different from the current node
            if not (np.array_equal(sonGameBoard, currentNode.getGameBoard())):
                self.avoidGoingBack(currentNode, queue,
                                    sonGameBoard, sonMarioPos, self.UP)
           # print(list(map(lambda x: x.getMarioPos(), queue)))
            #print("length of queue", len(queue))
            # for element in queue:
            #  print(element.getGameBoard())
        print("Mario Pos:", currentNode.getMarioPos())
        print("currentNodeCost: ", currentNode.getCost())
        print(currentNode.getDepth())

    def searchByCost(self):

        queue = []
        initialNode = node.Node(self.state, None, None, 0, self.marioPos)
        queue.append(initialNode)

        while True:

            if len(queue) == 0:
                print("Falló, vas a perder IA")

            # currentNode is now initial node and queue becomes empty
            currentNode = queue.pop(self.selectNodeByCost(queue))
            # Checks if the position of Mario equals Yoshi's
            if currentNode.goalReached(self.yoshiPos):
                self.findSolution(currentNode)
                break

            # expand currentNode with the possible directions
            sonGameBoard, sonMarioPos = currentNode.move(self.LEFT)
            # Check if new node is different from the current node
            if not (np.array_equal(sonGameBoard, currentNode.getGameBoard())):
                self.avoidGoingBack(currentNode, queue,
                                    sonGameBoard, sonMarioPos, self.LEFT)

            sonGameBoard, sonMarioPos = currentNode.move(
                self.DOWN)
            # Check if new node is different from the current node
            if not (np.array_equal(sonGameBoard, currentNode.getGameBoard())):
                self.avoidGoingBack(currentNode, queue,
                                    sonGameBoard, sonMarioPos, self.DOWN)

            sonGameBoard, sonMarioPos = currentNode.move(
                self.RIGHT)
            # Check if new node is different from the current node
            if not (np.array_equal(sonGameBoard, currentNode.getGameBoard())):
                self.avoidGoingBack(currentNode, queue,
                                    sonGameBoard, sonMarioPos, self.RIGHT)

            sonGameBoard, sonMarioPos = currentNode.move(
                self.UP)
            # Check if new node is different from the current node
            if not (np.array_equal(sonGameBoard, currentNode.getGameBoard())):
                self.avoidGoingBack(currentNode, queue,
                                    sonGameBoard, sonMarioPos, self.UP)
           # print(list(map(lambda x: x.getMarioPos(), queue)))
            #print("length of queue", len(queue))
            # for element in queue:
            #  print(element.getGameBoard())
        print("Mario Pos:", currentNode.getMarioPos())
        print("currentNodeCost: ", currentNode.getCost())
        print(currentNode.getDepth())

    def searchByDepth(self):
        stack = []
        initialNode = node.Node(self.state, None, None, 0, self.marioPos)
        stack.append(initialNode)

        while True:
            if len(stack) == 0:
                print("Falló, vas a perder IA")

            # currentNode is now initial node and queue becomes empty
            currentNode = stack.pop()
            if (currentNode.getDepth() > 0):
                print("Mi costo es", currentNode.getCost(
                ), "y la posición de mi padre es ", currentNode.getFather().getMarioPos())
            # Checks if the position of Mario equals Yoshi's
            if currentNode.goalReached(self.yoshiPos):
                self.findSolution(currentNode)
                break

             # expand currentNode with the possible directions
            sonGameBoard, sonMarioPos = currentNode.move(self.LEFT)
            # Check if new node is different from the current node
            if not (np.array_equal(sonGameBoard, currentNode.getGameBoard())):
                self.avoidGoingBack(currentNode, stack,
                                    sonGameBoard, sonMarioPos, self.LEFT)

            sonGameBoard, sonMarioPos = currentNode.move(
                self.DOWN)
            # Check if new node is different from the current node
            if not (np.array_equal(sonGameBoard, currentNode.getGameBoard())):
                self.avoidGoingBack(currentNode, stack,
                                    sonGameBoard, sonMarioPos, self.DOWN)

            sonGameBoard, sonMarioPos = currentNode.move(
                self.RIGHT)
            # Check if new node is different from the current node
            if not (np.array_equal(sonGameBoard, currentNode.getGameBoard())):
                self.avoidGoingBack(currentNode, stack,
                                    sonGameBoard, sonMarioPos, self.RIGHT)

            sonGameBoard, sonMarioPos = currentNode.move(
                self.UP)
            # Check if new node is different from the current node
            if not (np.array_equal(sonGameBoard, currentNode.getGameBoard())):
                self.avoidGoingBack(currentNode, stack,
                                    sonGameBoard, sonMarioPos, self.UP)

            print("Mario Pos:", currentNode.getMarioPos())
            print("currentNodeCost: ", currentNode.getCost())
            print(currentNode.getDepth())

    def selectNodeByCost(self, queue):

        nodeSelected = queue[0]
        nodeIndex = 0
        # simple movement
        for index, node in enumerate(queue):
            if nodeSelected.getCost() > node.getCost():
                nodeSelected = node
                nodeIndex = index

        return nodeIndex

    def findSolution(self, currentNode):
        solutions = []
        costos = []
        while currentNode != None:
            currentGameBoard = currentNode.getGameBoard()
            solutions.append(currentGameBoard)
            costos.append(currentNode.getCost())
            currentNode = currentNode.getFather()
        solutionsOrdered = solutions[::-1]
        costsF = costos[::-1]
        self.solution = solutionsOrdered
        print(costsF)
        # print(solutionsOrdered)

    def getSolution(self):
        return self.solution
