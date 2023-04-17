# pyright: strict

import pygame
from pygame.math import Vector2
from pygame.color import Color
from pygame.surface import Surface
from pygame.rect import Rect

screen = pygame.display.set_mode((800, 600))

RED = Color(255, 50, 50)
YELLOW = Color(255, 255, 50)
GREEN = Color(50, 255, 50)
CYAN = Color(50, 255, 255)
BLUE = Color(50, 50, 255)
WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)

class Brush:
	color: Color
	size: int

	def __init__(self, color: Color, size: int = 1) -> None:
		self.color = color
		self.size = size

	def paint(self, prev_mouse_pos: Vector2, layer: Surface = screen):
		mouse_pos = Vector2(pygame.mouse.get_pos())
		pygame.draw.line(layer, self.color, mouse_pos, prev_mouse_pos, self.size)


class Button:
	color: Color
	rect: Rect

	def __init__(self, color: Color, position: Vector2):
		self.color = color
		self.rect = Rect(position, Vector2(50, 50))

		pygame.draw.rect(pygame.display.get_surface(), self.color, self.rect)


class ColorButton(Button):
	def __init__(self, color: Color, position: Vector2):
		super().__init__(color, position)
class brushbutton(Button):
	def __init__(self, color: Color, position: Vector2):
		super().__init__(color, position)

# Start of code that does stuff

screen.fill(Color(200, 200, 200))

buttons = [ColorButton(RED, Vector2(0, 0)), ColorButton(GREEN, Vector2(50, 0)), ColorButton(YELLOW, Vector2(100, 0)),
]

brush = Brush(RED)

# Main Loop
running = True
prev_mouse_pos = pygame.mouse.get_pos()
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	if pygame.mouse.get_pressed()[0]:
		for button in buttons:
			if type(button) == ColorButton and button.rect.collidepoint(pygame.mouse.get_pos()):
				brush.color = button.color
		for button in buttons:
			if type(button) == brushbutton and button.rect.collidepoint(pygame.mouse.get_pos()):
				brush.size = 10
		brush.paint(Vector2(prev_mouse_pos))

	pygame.display.flip()

	prev_mouse_pos = pygame.mouse.get_pos()
