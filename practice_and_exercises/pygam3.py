import pygame
import sys

pygame.init()

#Colores en RGB
negro = (0, 0, 0)
blanco = (255, 255, 255)
rojo = (210, 0, 0)
morado = (101, 0, 106)
azul = (0, 29, 106)

size = (800, 600)

#Para crear la ventana
screen = pygame.display.set_mode(size)

#Tratando de cargar imagenes
imagen = pygame.image.load('bg.jpg')

while True:
    #Se agrega lo siguiente para que se pueda cerrar la ventana:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(imagen, [0,0])       #Define la posicion de la imagen
    
    #Dibujando figuras
    pygame.draw.line(screen, rojo, [50, 250], [200, 250], 10) 
    pygame.draw.polygon(screen, morado, [(20, 80), (120, 180), (220, 80)], 0)
    
    #Dibujando con for loops
    for i in range(100, 900, 150):
        pygame.draw.circle(screen, blanco, (i,350), 50)
    
    pygame.display.flip()      #Actualiza el display