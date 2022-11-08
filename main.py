import viewer
import gameBoard as gb
import numpy as np

test = np.loadtxt("Prueba1.txt", dtype='i', delimiter=' ')
search = "profundidad"

gameBoard = gb.GameBoard(test)
# find Mario and Yoshi
gameBoard.findPeople()

if search == "amplitud":
    gameBoard.searchByAmplitude()
if search == "costo uniforme":
    gameBoard.searchByCost()
if search == "profundidad":
    gameBoard.searchByDepth()

solution = gameBoard.getSolution()
viewer = viewer.Viewer(solution)
viewer.drawState()
