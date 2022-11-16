import searchAlgorithm as SA
import numpy as np


class Controller():

    def __init__(self, searchBy):
        self.test = np.loadtxt("Prueba1.txt", dtype='i', delimiter=' ')
        # amplitud, costo uniforme, profundidad, avara, A*
        self.searchBy = searchBy
        self.solution = []
        self.searchAlgorithm = SA.SearchAlgorithm(self.test)
        # find Mario and Yoshi
        self.searchAlgorithm.findPeople()
        self.depth = 0
        self.generatedNodes = 0
        self.expandedNodes = 0
        self.cost = 0
        self.algorithmTime = ""

    def search(self):
        # find solution using algorithm selected
        self.searchAlgorithm.search(self.searchBy)
        # return the solution found
        self.solution = self.searchAlgorithm.getSolution()
        self.depth = self.searchAlgorithm.getDepth()
        self.generatedNodes = self.searchAlgorithm.getGeneratedNodes()
        self.expandedNodes = self.searchAlgorithm.getExpandedNodes()
        self.cost = self.searchAlgorithm.getCost()
        self.algorithmTime = str(self.searchAlgorithm.getAlgorithmTime())

    def getSolution(self):
        return self.solution
        #boardViewer = boardViewer.Viewer(solution)
        # boardViewer.drawState()

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
