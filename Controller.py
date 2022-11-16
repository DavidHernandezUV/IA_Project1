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

    def search(self):
        # find solution using algorithm selected
        self.searchAlgorithm.search(self.searchBy)
        # return the solution found
        self.solution = self.searchAlgorithm.getSolution()

    def getSolution(self):
        return self.solution
        #boardViewer = boardViewer.Viewer(solution)
        # boardViewer.drawState()
