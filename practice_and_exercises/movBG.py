import pygame
import sys

pygame.init()

w, h = 800, 600
screen = pygame.display.set_mode((w, h))

bg = pygame.image.load("bg.jpg").convert()
x = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	x_relativa = x % screen.get_rect().width
	screen.blit(bg, (x_relativa - screen.get_rect().width, 0))
	if x_relativa < w:
		screen.blit(bg, (x_relativa, 0))
	x -= 1
	pygame.display.update()
