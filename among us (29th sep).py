import random
import pygame
from pygame import mouse
from pygame.rect import Rect
from pygame.math import Vector2
from pygame.color import Color
from pygame.surface import Surface

WIDTH = 1200
HEIGHT = 900

N_TARGETS = 4

MAX_TIME = 5

END_DELAY = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

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
		Color("#e44142"),
		Color("#e3b934"),
		Color("#3bc74d"),
		Color("#3490e4")
	]

	bounds :Rect
	colorname :int

	def __init__(self, pos :tuple[float, float], color :int, size :tuple[float, float] = (110, 100)):
		self.pos = Vector2(pos)
		self.colorname = color
		self.color = self.COLORS[color]
		self.bounds = Rect(pos, size)

	def draw(self, surface :Surface):
		pygame.draw.rect(surface, self.color, self.bounds, 0, 4)

class Wire(GameObject):
	start :Vector2
	end :Vector2
	width :int

	def __init__(self, start :tuple[float, float], end :tuple[float, float], color :Color, width :int):
		self.start = Vector2(start)
		self.end = Vector2(end)
		self.color = color
		self.width = width
		

	def draw(self, surface :Surface):
		pygame.draw.line(surface, self.color, self.start, self.end, self.width)


# Game setup:

clock = pygame.time.Clock()
objects :list[GameObject] = []
for x in [-10, WIDTH-100]:
	colorlist = [Target.RED, Target.YELLOW, Target.GREEN, Target.BLUE]
	assert len(colorlist) == N_TARGETS
	random.shuffle(colorlist)
	for y in [100, 300, 500, 700]:
		objects.append(Target((x, y), colorlist.pop()))

start_point :Vector2 | None = None
start_color :int = -1

just_pressed = False
just_released = False

wires_completed :list[bool] = [False, False, False, False]

start_time = pygame.time.get_ticks()

game_font = pygame.font.SysFont("consolas", 64)
text = ""


# Main loop:

game_over :float | None = None
running = True
while running:
	clock.tick(75)
	elapsed = (pygame.time.get_ticks() - start_time) / 1000
	if game_over == None:
		text = str(round(elapsed, 1))

	# Input:
	just_pressed = False
	just_released = False
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			running = False
		elif e.type == pygame.MOUSEBUTTONDOWN:
			just_pressed = True
		elif e.type == pygame.MOUSEBUTTONUP:
			just_released = True

	# Update:
	if game_over == None: # don't bother game objects if the game has ended
		for o in objects:
			o.update(clock.get_time() / 1000)

			if type(o) is Target and o.bounds.collidepoint(mouse.get_pos()):
				if just_pressed:
					start_point = Vector2(o.bounds.center)
					start_color = o.colorname
				elif just_released and start_point != None and o.colorname == start_color and start_point != Vector2(o.bounds.center):
						objects.append(Wire((start_point.x, start_point.y), (o.bounds.centerx, o.bounds.centery), Target.COLORS[start_color].lerp((0, 0, 0), 0.2), 16))
						wires_completed[o.colorname] = True

		complete = True
		for c in wires_completed:
			if not c:
				complete = False
			
		if complete: # game is won
			text = "You won! (time: {}s)".format(round(elapsed, 1))
			game_over = END_DELAY
		elif elapsed > MAX_TIME: # game is lost
			text = "You lost. Better luck next time?"
			game_over = END_DELAY
	else:
		assert type(game_over) is float

		game_over -= clock.get_time() / 1000
		if game_over <= 0:
			running = False

	# Draw:
	screen.fill(Color(20, 20, 20))
	for o in objects:
		o.draw(screen)

	if start_point != None:
		pygame.draw.line(screen, Target.COLORS[start_color].lerp((255, 255, 255), 0.2), start_point, mouse.get_pos(), 16)

	display_text = game_font.render(text, True, Color(255, 255, 255))
	screen.blit(display_text, ((WIDTH / 2) - (display_text.get_rect().width / 2), HEIGHT - 100))

	pygame.display.flip()

	# Prepare next frame:
	if just_released:
			start_point = None
			start_color = -1

