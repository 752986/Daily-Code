import pygame
import math

pygame.init()
screen = pygame.display.set_mode((640 * 2, 480 * 2))

def buildingfloor(pos: tuple[float, float], dims: tuple[float, float], windowsize: float, windowspacing: float, color, windowcolor):
    pygame.draw.rect(screen, color, pygame.Rect(pos[0], pos[1], dims[0], dims[1]))

    nwindows = math.floor(dims[0] / (windowsize + windowspacing))
    for i in range(nwindows):
        extraspace = dims[0] - ((windowsize + windowspacing) * nwindows)
        drawx = (i * windowsize) + ((i + 0.5) * windowspacing) + (extraspace / 2)
        drawy = (dims[1] - windowsize) / 2
        pygame.draw.rect(screen, windowcolor, pygame.Rect(pos[0] + drawx, pos[1] + drawy, windowsize, windowsize))

def building(pos: tuple[float, float], dims: tuple[float, float], nfloors: int, colors: tuple):
    floorheight = dims[1] / nfloors
    for i in range(nfloors):
        buildingfloor((i * floorheight) + pos)


######
buildingfloor((50, 100), (120, 40), 30, 5, (0, 100, 200), (100, 200, 100))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()