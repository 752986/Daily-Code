import random
import pygame
from pygame import mouse
from pygame.rect import Rect
from pygame.math import Vector2
from pygame.color import Color
from pygame.surface import Surface

pygame.init()
screen = pygame.display.set_mode((1200, 900))


# Class definitions:

class GameObject:
	pos :Vector2
	color :Color
	should_delete :bool

	def update(self, delta :float):
		pass

	def draw(self, surface :Surface):
		pass

class Target(GameObject):
	RED = 0
	YELLOW = 1
	GREEN = 2
	BLUE = 3

	COLORS = [
		Color(200, 100, 100),
		Color(200, 200, 100),
		Color(100, 200, 100),
		Color(100, 100, 200)
	]

	bounds :Rect
	colorname :int

	def __init__(self, pos :tuple[float, float], color :int, size :tuple[float, float] = (200, 100)):
		self.pos = Vector2(pos)
		self.colorname = color
		self.color = self.COLORS[color]
		self.bounds = Rect(pos, size)

	def update(self, delta :float):
		pass


	def draw(self, surface :Surface):
		pygame.draw.rect(surface, self.color, self.bounds, 0, 4)


# Game setup:
clock = pygame.time.Clock()
objects :list[GameObject] = []
for x in [100, 900]:
	colorlist = random.shuffle([Target.RED, Target.YELLOW, Target.GREEN, Target.BLUE])
	for y in [100, 300, 500, 700]:
		objects.append(Target((x, y), colorlist.pop()))

startpoint :Vector2 | None = None
startcolor :int | None

just_pressed = False

# Main loop:
running = True
while running:
	clock.tick(75)

	# Input:
	just_pressed = False
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			running = False
		elif e.type == pygame.MOUSEBUTTONDOWN:
			just_pressed = True
		elif e.type == pygame.MOUSEBUTTONUP:
			startpoint = None

	# Update:
	for o in objects:
		o.update(clock.get_time() / 1000)

		if just_pressed and type(o) is Target and o.bounds.collidepoint(mouse.get_pos()):
			startpoint = Vector2(mouse.get_pos())
			startcolor = o.colorname

	# Draw:
	screen.fill(Color(20, 20, 20))
	for o in objects:
		o.draw(screen)

	if startpoint != None:
		pygame.draw.line(screen, Target.COLORS[startcolor], startpoint, mouse.get_pos(), 4)
	
	pygame.display.flip()