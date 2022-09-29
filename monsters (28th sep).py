import pygame
import math
import random
pygame.init

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("monster gen with inheritance")

# function definition for circular collision-------------------------------------------
def CircularCollision(x1, y1, x2, y2, radius = 50): #polymorphism! wow!
    x1 += 16  # adjust so center is not top left corner
    y1 += 16
    if math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)) < radius:
        return True
    else:
        return False

class GameObject():
    x: float
    y: float
    image: pygame.surface.Surface

    def update(self, clock):
        pass

    def draw(self, surface = screen):
        pass

    def should_delete(self):
        pass

monsterlist: list[GameObject] = []  # a list to hold all the monsters the monstergen makes


# parent class-------------------------------------------------------------------------
class Heart(GameObject):
    image = pygame.transform.scale(pygame.image.load("./res/fcd0300deb4fd92735c20a6ea91ec1ca.png"), (20, 20))

    def __init__(self, x: float, y: float, vx: float, vy: float):
        self.x = x
        self.y = y
        self.vx = (random.random() - 0.5) * vx
        self.vy = vy
        self.vxscale = vx * 0.3

    def update(self, clock):
        self.x += self.vx
        self.y += self.vy
        self.vx += (random.random() - 0.5) * self.vxscale

    def draw(self, surface = screen):
        surface.blit(self.image, (self.x, self.y))

    def should_delete(self) -> bool:
        return not (screen.get_rect().colliderect(((self.x, self.y), (20, 20))))


class Hand(GameObject):
    HAND_SPEED = 300
    image1 = pygame.transform.scale(pygame.image.load("./res/frame_0_delay-0.05s.gif"), (50, 50))
    image2 = pygame.transform.scale(pygame.image.load("./res/frame_2_delay-0.05s.gif"), (50, 50))
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = self.image1
        self.image.set_colorkey((255, 255, 255))
        self.image = self.image2
        self.image.set_colorkey((255, 255, 255))
        self.accum = 0.0

    def update(self, clock):
        self.x = pygame.mouse.get_pos()[0] - 25
        self.y = pygame.mouse.get_pos()[1] - 20

        self.accum += clock.get_time()

        if not pygame.mouse.get_pressed()[0]:
            self.image = self.image2
        else:
            if self.accum % self.HAND_SPEED > self.HAND_SPEED / 2:
                self.image = self.image1
            else:
                self.image = self.image2

    def draw(self, surface = screen):
        surface.blit(self.image, (self.x, self.y))

    def should_delete(self) -> bool:
        return False
    
class Monster(GameObject):
    def __init__(self, x: int, y: int, image: str, size: float): # constructor
        self.x: int = x
        self.y: int = y
        self.health: int = random.randint(400, 3000)
        self.alive: bool = True
        self.image: pygame.surface.Surface = pygame.image.load(image)
        self.bounds: pygame.rect.Rect = pygame.rect.Rect((self.x, self.y), (self.image.get_width() * size, self.image.get_height() * size))
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * size, self.image.get_height() * size))

    def emitParticle(self):
        h = Heart(pygame.mouse.get_pos()[0] + random.randint(-20, 20), pygame.mouse.get_pos()[1] + random.randint(-20, 20), 2, -4)
        monsterlist.append(h)

    def getClicked(self):
        if self.alive and pygame.mouse.get_pressed()[0] and self.bounds.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
            print(random.choice(["💖", "🥰", "😊", "✨", "\n"]), end="")
            self.health -= 10
            self.emitParticle()

    def update(self, clock):
        self.getClicked()
        if self.health <= 0 and self.alive:
            print("\n Bye for now!")
            self.alive = False

    def should_delete(self) -> bool:
        return self.health <= 0

    def draw(self, surface: pygame.surface.Surface = screen):
        if self.alive:  # dont draw ded monsters
            surface.blit(self.image, (self.x, self.y))


# child class--------------------------------------------------------------------------
class Creeper(Monster):
    def __init__(self, x: int, y: int):
        # call constructor of parent class
        super().__init__(x, y, "./res/GUEST_ac7896ab-ec5c-4e4b-b428-b1c563084cde.jpg", 0.2)
        self.image.set_colorkey((255, 255, 255))
        

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
hand = Hand()
monsterlist.append(hand)

# creates game screen and caption


# game variables
doExit = False  # variable to quit out of game loop
clock = pygame.time.Clock()  # sets up a game clock to regulate game speed
pos = pygame.mouse.get_pos()
pygame.mouse.set_visible(False)
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
    for o in monsterlist:
        o.update(clock)
        if o.should_delete():
            monsterlist.remove(o)

    # render section-----------------------------------

    # redraw black background
    screen.fill((0, 0, 0))

    # c1.draw() #draw the test creeper

    # draw all the monsters in the list
    for i in range(len(monsterlist)):
        monsterlist[i].draw()
    # draw the cursor on top:
    hand.draw()

    pygame.display.flip()  # update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()
