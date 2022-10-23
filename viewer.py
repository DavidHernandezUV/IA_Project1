import pygame, sys, math
import numpy as np


class Viewer:

    #Constructor
    def __init__(self, initial_state):

        self.initial_state = initial_state;
        
        #Window dimensions
        self.w_height = 600
        self.w_width = 600

        self.blockSize = math.floor(self.w_width/10)

        self.size = (self.w_height,self.w_width)
        #self.test = np.loadtxt("Prueba1.txt", dtype='i',delimiter=' ')

        #Colors
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)


    def drawState(self):
        pygame.init()

        #Create window
        screen = pygame.display.set_mode(self.size)
        screen.fill(self.WHITE)
        self.figures(screen,self.initial_state)



        while True:
                
            self.drawGrid(screen)
            for event in pygame.event.get(): #registrar lo que sucede en la ventana
                #print(event)
                if event.type == pygame.QUIT:
                    sys.exit()
                
            ##----DRAW ZONE
                
            #pygame.draw.line(screen,BLACK,[0,0],[100,100],5)

            ##----DRAW ZONE

            #world update
            pygame.display.update()

    def drawGrid(self, screen):
        
        for x in range(0,self.w_width,self.blockSize):
            for y in range(0,self.w_height,self.blockSize):
                rect = pygame.Rect(x,y,self.blockSize,self.blockSize)
                pygame.draw.rect(screen,self.BLACK,rect,1)

    def figures(self, screen, matriz):

        aux = np.nditer(matriz,flags=['multi_index'])
        for element in aux:
            #print(aux.multi_index)
            #print("%d %s" % (element, aux.multi_index), end=' ')
            if element!=0:
                
                
                fig = pygame.image.load("img/%d.jpg" % int(element)).convert()
                # Using blit to copy content from one surface to other
                screen.blit(fig, (aux.multi_index[1]*self.blockSize+5, aux.multi_index[0]*self.blockSize+5))

        
