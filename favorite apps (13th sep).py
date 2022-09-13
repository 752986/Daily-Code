import pygame
import random

pygame.init()

screen = pygame.display.set_mode((450, 900))


# the width / height of an app icon
APPSIZE = 100

class App:
	box: pygame.Rect
	color: pygame.Color

	def __init__(self, pos: tuple[int, int], color):
		self.box = pygame.Rect(pos, (APPSIZE, APPSIZE))
		self.color = color

	def draw(self):
		pygame.draw.rect(screen, self.color, self.box, 0, 8)


# create list of app icons:
applist: list[App] = []
APPOFFSET = (55, 350)

for i in range(3):
	for j in range(3):
		color = pygame.Color(0, 0, 0)
		color.hsva = (random.randint(0, 359), random.randint(30, 70), 75, 100)
		applist.append(App((i * (APPSIZE + 20) + APPOFFSET[0], j * (APPSIZE + 20) + APPOFFSET[1]), color))


# initialize click count dictionary
appcount = dict(zip(applist, [0 for i in applist]))


# main loop:
running = True
while running:
	# input:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			running = False
		elif e.type == pygame.MOUSEBUTTONDOWN:
			for app in applist:
				if app.box.collidepoint(pygame.mouse.get_pos()):
					appcount[app] += 1
				print(appcount[app])
			print()

	# find top apps:
	topapps = sorted(appcount, key=lambda x:appcount[x], reverse=True)

	favapps: list[App] = []
	for i in range(3):
		favapps.append(App((i * (APPSIZE + 20) + APPOFFSET[0], 20), topapps[i].color))

	# draw:
	screen.fill((48, 52, 70))
	pygame.draw.rect(screen, (41, 44, 60), pygame.Rect(0, 0, screen.get_width(), 140))

	for app in applist:
		app.draw()
	for app in favapps:
		app.draw()

	pygame.display.flip()

pygame.quit()