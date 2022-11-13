import boardViewer
import gameBoard as gb
import numpy as np

test = np.loadtxt("Prueba1.txt", dtype='i', delimiter=' ')
search = "A*"

gameBoard = gb.GameBoard(test)
# find Mario and Yoshi
gameBoard.findPeople()

if search == "amplitud":
    gameBoard.searchByAmplitude()
if search == "costo uniforme":
    gameBoard.searchByCost()
if search == "profundidad":
    gameBoard.searchByDepth()
if search == "avara":
    gameBoard.greedySearch()
if search == "A*":
    gameBoard.AStarSearch()


solution = gameBoard.getSolution()
boardViewer = boardViewer.Viewer(solution)
boardViewer.drawState()
