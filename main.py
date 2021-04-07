import pygame
pygame.init()

screen = pygame.display.set_mode((720, 1440))
running = True

#colours
red = (255, 0, 0)
green = (0, 170, 0)
blue = (0, 0, 255)
orange = (200, 145, 0)
magenta = (255, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (140, 140, 140)
cyan = (0, 255, 255)
yellow = (255, 255, 0)

#circles
r1, r2 = 100, 1
speed = 10
j = 0

while running:
	screen.fill((127.5, 127.5, 255))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	#circles
	pygame.draw.circle(screen, blue, (360, 720), r1)
	pygame.draw.circle(screen, yellow, (360, 720), r2)
	
	#zoom in
	if j >= 40:
		r1 += speed
		r2 += speed/100

	#timer
	j += 1
	pygame.display.flip()

pygame.quit()
