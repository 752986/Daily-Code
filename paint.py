# pyright: strict

import pygame
from pygame.math import Vector2
from pygame.color import Color
from pygame.surface import Surface

screen = pygame.display.set_mode((800, 600))

class Brush:
	color: Color
	size: int

	def __init__(self, color: Color, size: int = 1) -> None:
		self.color = color
		self.size = size

	def paint(self, layer: Surface = screen):
		mouse_pos = Vector2(pygame.mouse.get_pos())
		mouse_rel = Vector2(pygame.mouse.get_rel())
		pygame.draw.line(layer, self.color, mouse_pos, mouse_pos - mouse_rel, self.size)


brush = Brush(Color(10, 20, 15))

# Main Loop
while True:
