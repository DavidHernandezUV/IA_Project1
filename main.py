import boardViewer
import searchAlgorithm as SA
import numpy as np

test = np.loadtxt("Prueba1.txt", dtype='i', delimiter=' ')
# amplitud, costo uniforme, profundidad, avara, A*
search = "A*"

searchAlgorithm = SA.SearchAlgorithm(test)
# find Mario and Yoshi
searchAlgorithm.findPeople()

searchAlgorithm.search(search)


solution = searchAlgorithm.getSolution()
boardViewer = boardViewer.Viewer(solution)
boardViewer.drawState()
