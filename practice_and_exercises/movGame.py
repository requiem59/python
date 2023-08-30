import pygame
import sys

pygame.init()

negro = (0, 0, 0)
blanco = (255, 255, 255)
rojo = (210, 0, 0)
morado = (101, 0, 106)
azul = (0, 29, 106)

win = pygame.display.set_mode((800, 600))
reloj = pygame.time.Clock()

cirx = 400
ciry = 300

vcirx = 2
vciry = 2

while(True):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    win.fill(negro)
    pygame.draw.circle(win, morado, (cirx, ciry), 30)
    
    if(cirx > 770 or cirx < 30):
        vcirx *= -1
        
    if(ciry > 570 or ciry < 30):
        vciry *= -1
    
    cirx += vcirx
    ciry += vciry
    
    pygame.display.flip()  
    reloj.tick(60)