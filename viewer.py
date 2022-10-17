import pygame, sys, math
import numpy as np



#Window dimensions
w_height = 600
w_width = 600

size = (w_height,w_width )
test = np.loadtxt("Prueba1.txt", dtype='i',delimiter=' ')

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

def main():
    pygame.init()

    #Create window
    screen = pygame.display.set_mode(size)
    screen.fill(WHITE)
    figures(screen,test)



    while True:
        
        drawGrid(screen)
        for event in pygame.event.get(): #registrar lo que sucede en la ventana
            #print(event)
            if event.type == pygame.QUIT:
                sys.exit()
        
        ##----DRAW ZONE
        
        #pygame.draw.line(screen,BLACK,[0,0],[100,100],5)

        ##----DRAW ZONE

        #world update
        pygame.display.update()

def drawGrid(screen):
    blockSize = math.floor(w_width/10)
    for x in range(0,w_width,blockSize):
        for y in range(0,w_height,blockSize):
            rect = pygame.Rect(x,y,blockSize,blockSize)
            pygame.draw.rect(screen,BLACK,rect,1)

def figures(screen, matriz):

    aux = np.nditer(matriz,flags=['multi_index'])
    print(aux)
    for element in aux:
                
                if element!=0:
                    print("%d %s" % (element, aux.multi_index), end=' ')
                    #print("img/"+str(element)+ ".jpg")
                    fig = pygame.image.load("img/%d.jpg" % int(element)).convert()
                    # Using blit to copy content from one surface to other
                    screen.blit(fig, (aux.multi_index[1]*60+5, aux.multi_index[0]*60+5))

main()
