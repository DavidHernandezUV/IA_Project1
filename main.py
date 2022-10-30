import viewer
import gameBoard as gb
import numpy as np

test = np.loadtxt("Prueba1.txt", dtype='i', delimiter=' ')
viewer = viewer.Viewer(test)
# viewer.drawState()
search = "amplitud"

gameBoard = gb.GameBoard(test)
# find Mario and Yoshi
gameBoard.findPeople()

if search == "amplitud":
    gameBoard.searchByAmplitude()
