import pygame
import math
import random
pygame.init

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("monster gen with inheritance")

monsterlist = []  # a list to hold all the monsters the monstergen makes

# function definition for circular collision-------------------------------------------
def CircularCollision(x1, y1, x2, y2):
    x1 += 16  # adjust so center is not top left corner
    y1 += 16
    if math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)) < 50:
        return True
    else:
        return False

# parent class-------------------------------------------------------------------------


class Monster():

    def __init__(self, x: int, y: int, image: str, size: float):  # constructor
        self.xpos: int = x
        self.ypos: int = y
        self.health: int = 1000
        self.alive: bool = True
        self.size = size
        self.image: pygame.surface.Surface = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * self.size, self.image.get_height() * self.size))


    def getClicked(self):
        if CircularCollision(self.xpos, self.ypos, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]) == True and self.alive:
            print("hit!")
            self.health -= 10

    def ded(self):
        if self.health <= 0 and self.alive:
            print("I'm ded.")
            self.alive = False

    def draw(self, surface: pygame.surface.Surface = screen):
        if self.alive:  # dont draw ded monsters
            surface.blit(self.image, (self.xpos, self.ypos))


# child class--------------------------------------------------------------------------
class Creeper(Monster):
    def __init__(self, x: int, y: int):
        # call constructor of parent class
        super().__init__(x, y, "./res/GUEST_ac7896ab-ec5c-4e4b-b428-b1c563084cde.jpg", 0.2)
        

# add more child classes here!

class Spider(Monster):
    def __init__(self, x: int, y: int):
        # call constructor of parent class
        super().__init__(x, y, "./res/D2DdwMzX4AAG7q4.jpg", 0.05)

class Zombie(Monster):
    def __init__(self, x: int, y: int):
        # call constructor of parent class
        super().__init__(x, y, "./res/minecraft_fanart___zombie_by_devburmak_d4dkoar-fullview.jpg", 0.15)

class Skeleton(Monster):
    def __init__(self, x: int, y: int):
        # call constructor of parent class
        super().__init__(x, y, "./res/Sans_undertale.jpg", 0.3)        

# Monster gen function definition------------------------------------------------------


def MonsterGen():
    num = random.randrange(0, 100)
    if num < 20:
        monsterlist.append(
            Creeper(random.randrange(0, 750), random.randrange(0, 750)))
    elif num < 50:
       monsterlist.append(Spider(random.randrange(0, 500), random.randrange(0, 500)))
    elif num < 80:
       monsterlist.append(Zombie(random.randrange(0, 500), random.randrange(0, 500)))
    else:
       monsterlist.append(Skeleton(random.randrange(0, 500), random.randrange(0, 500)))

# ---------------------------------------------------------------------------------------------

# creation of an object variable or an instance for testing (most of the others are made by the monster gen)
#c1 = Creeper(200, 200)


# use monstergen to make the others
for i in range(20):
    MonsterGen()

# creates game screen and caption


# game variables
doExit = False  # variable to quit out of game loop
clock = pygame.time.Clock()  # sets up a game clock to regulate game speed
pos = pygame.mouse.get_pos()
click = False

#BEGIN GAME LOOP######################################################
while not doExit:

    # input section-----------------------------------
    clock.tick(60)  # FPS (frames per second)

    # pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True  # lets you quit program

        if event.type == pygame.MOUSEBUTTONDOWN:  # get and store mouse input
            click = True

        if event.type == pygame.MOUSEBUTTONUP:  # get and store mouse input
            click = False

    if click == True:
        pos = pygame.mouse.get_pos()

    # physics section----------------------------------
    for i in range(len(monsterlist)):
        monsterlist[i].getClicked()
        monsterlist[i].ded()

    # render section-----------------------------------

    # redraw black background
    screen.fill((0, 0, 0))

    # c1.draw() #draw the test creeper

    # draw all the monsters in the list
    for i in range(len(monsterlist)):
        monsterlist[i].draw()

    pygame.display.flip()  # update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()
