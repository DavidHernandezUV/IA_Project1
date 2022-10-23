import viewer
import numpy as np

test = np.loadtxt("Prueba1.txt", dtype='i', delimiter=' ')
viewer = viewer.Viewer(test)
viewer.drawState()
