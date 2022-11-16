import copy

import numpy as np

import node

import time


class SearchAlgorithm:
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
        self.generatedNodes = 1
        self.expandedNodes = 0
        self.depth = 0
        self.cost = 0
        self.algorithmTime = ""
        # in depth algorithm, it starts from the last direction: the last is the first it checks
        self.directions = [self.RIGHT, self.LEFT, self.DOWN, self.UP]

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
                self.generatedNodes += 1
                queue.append(node.Node(sonGameBoard, currentNode, direction,
                                       currentNode.getDepth()+1, sonMarioPos, self.yoshiPos))
        # If the node is the initial node, the new node is added without checking if it can go back
        else:
            self.generatedNodes += 1
            queue.append(node.Node(sonGameBoard, currentNode, direction,
                                   currentNode.getDepth()+1, sonMarioPos, self.yoshiPos))

    def avoidLoops(self, currentNode, queue, sonGameBoard, sonMarioPos, direction):

        Loops = False
        copyNode = copy.deepcopy(currentNode)
        while currentNode.getDepth() != 0:

            if (np.array_equal(sonGameBoard, currentNode.getFather().getGameBoard())):
                Loops = True
                break

            currentNode = currentNode.getFather()

        if not Loops:
            self.generatedNodes += 1
            queue.append(node.Node(sonGameBoard, copyNode, direction,
                                   copyNode.getDepth()+1, sonMarioPos, self.yoshiPos))

    def avoid(self, select):
        if select == "goingBack":
            return self.avoidGoingBack
        elif select == "loops":
            return self.avoidLoops

    def selectNodeBy(self, algorithm, list):
        # queue
        if algorithm == "amplitud":
            return list.pop(0)
        # prioritized queue by cost
        elif algorithm == "costo uniforme":
            return list.pop(self.selectNodeByCost(list))
        # stack
        elif algorithm == "profundidad":
            return list.pop()
        # prioritized queue by heuristic
        elif algorithm == "avara":
            return list.pop(self.selectNodeByHeuristic(list))
        # prioritized queue by cost + heuristic
        elif algorithm == "A*":
            return list.pop(self.selectNodeByAStar(list))

    def search(self, algorithm):
        startTime = time.time()
        list = []  # it can be a queue or a stack
        initialNode = node.Node(self.state, None, None,
                                0, self.marioPos, self.yoshiPos)
        list.append(initialNode)

        while True:
            if len(list) == 0:
                print("Falló, vas a perder IA")

            # currentNode is now initial node and queue becomes empty
            currentNode = self.selectNodeBy(algorithm, list)

            # the node is about to be expanded
            self.expandedNodes += 1
            # Checks if the position of Mario equals Yoshi's
            if currentNode.goalReached(self.yoshiPos):
                endTime = time.time()
                self.algorithmTime = str(endTime - startTime)
                print("Tiempo de ejecución:", self.algorithmTime, "segundos")
                self.findSolution(currentNode)
                print("Mario Pos:", currentNode.getMarioPos())
                self.cost = currentNode.getCost()
                print("currentNodeCost: ", currentNode.getCost())
                self.depth = currentNode.getDepth()
                print("profundidad", self.depth)
                print("Nodos generados", self.generatedNodes)
                print("Nodos expandidos", self.expandedNodes)
                break

            if algorithm == "profundidad":
                avoidVar = "loops"
            else:
                avoidVar = "goingBack"

            # For that iterates over the four possible directions

            for direction in self.directions:
                # expand currentNode with the possible directions
                sonGameBoard, sonMarioPos = currentNode.move(direction)
                # Check if new node is different from the current node, this means the movement is NOT POSSIBLE
                if not (np.array_equal(sonGameBoard, currentNode.getGameBoard())):
                    self.avoid(avoidVar)(currentNode, list,
                                         sonGameBoard, sonMarioPos, direction)

    def selectNodeByCost(self, queue):

        nodeSelected = queue[0]
        nodeIndex = 0
        # simple movement
        for index, node in enumerate(queue):
            if nodeSelected.getCost() > node.getCost():
                nodeSelected = node
                nodeIndex = index

        return nodeIndex

    def selectNodeByHeuristic(self, queue):

        nodeSelected = queue[0]
        nodeIndex = 0
        # simple movement
        for index, node in enumerate(queue):

            if nodeSelected.getHeuristic() > node.getHeuristic():
                nodeSelected = node
                nodeIndex = index

        return nodeIndex

    def selectNodeByAStar(self, queue):
        nodeSelected = queue[0]
        nodeIndex = 0
        # simple movement
        for index, node in enumerate(queue):
           # print(nodeSelected.getMarioPos())
            if nodeSelected.getBest() > node.getBest():
                nodeSelected = node
                nodeIndex = index

        return nodeIndex

    def findSolution(self, currentNode):
        solutions = []
        costs = []
        heuristics = []
        while currentNode != None:
            currentGameBoard = currentNode.getGameBoard()
            solutions.append(currentGameBoard)
            costs.append(currentNode.getCost())
            heuristics.append(currentNode.getHeuristic())
            currentNode = currentNode.getFather()
        solutionsOrdered = solutions[::-1]
        #costsF = costs[::-1]
        #heuristicsF = heuristics[::-1]
        self.solution = solutionsOrdered
        #print("Costos", costsF)
        #print("Heuristicas", heuristicsF)
        # print(solutionsOrdered)

    def getSolution(self):
        return self.solution

    def getDepth(self):
        return self.depth

    def getGeneratedNodes(self):
        return self.generatedNodes

    def getExpandedNodes(self):
        return self.expandedNodes

    def getCost(self):
        return self.cost

    def getAlgorithmTime(self):
        return self.algorithmTime
