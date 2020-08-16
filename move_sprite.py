
import pygame
from pygame.locals import *
from random import choice, randrange
from glob import glob
import sys

# pos are the possible positions for the numbers
# pos = [(x, y) for x in range(1, 8) for y in range(1, 8)]
WINDOWWIDTH = w = 400
WINDOWHEIGHT = h = 400
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
pygame.display.set_caption("Astroid")
g = pygame.sprite.Group()
# num_order = []
score = 0
bgd = pygame.Surface((50, 50))
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(32)
# click = pygame.mixer.Sound("click.wav")
# chimp = pygame.image.load("img\\chimp.png")
counter = 0
counter_on: bool = 1
max_count = 100
cards_visible = 1

font = pygame.font.SysFont("Arial", 20)



class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Sprite, self).__init__()
        # self.number = str(number)
        self.x, self.y = x, y
        self.make_image()
        g.add(self)
        # del pos[pos.index(position)]

    def make_image(self):
        # self.image = pygame.Surface((50, 50))
        # r, g, b = [randrange(128, 256) for x in range(3)]
        # self.fill((r, g, b))
        # self.rect.center = self.x, self.y
        # self.text = font.render(self.number, 1, (0, 0, 0))
        # text_rect = self.tect.get_rect(center=(50 // 2, 50 // 2))
        # self.image.blit(self.text, text_rect)
        self.image = pygame.image.load("img/ship.png")
        self.rect = pygame.Rect(self.x, self.y, 128, 64)

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, 128, 64)

def hide():
    for s in g:
        bgd.fill((0, 240, 0))
        s.image.blit(bgd, (0, 0))
    # pos = [(x, y) for x in range(1, 8) for y in range(1, 8)]

def movements():
    "Move a surface"
    player = Sprite(10, 10)


    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False

    MOVESPEED = 1
    while True:
    # Check for events.
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                # Change the keyboard variables.
                if event.key == K_LEFT or event.key == K_a:
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == K_w:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == K_s:
                    moveUp = False
                    moveDown = True
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False

    # Draw the white background onto the surface.
        screen.fill((255, 255, 255))

        # Move the player.
        if moveDown and player.rect.bottom < WINDOWHEIGHT:
            player.rect.top += MOVESPEED
        if moveUp and player.rect.top > 0:
            player.rect.top -= MOVESPEED
        if moveLeft and player.rect.left > 0:
            player.rect.left -= MOVESPEED
        if moveRight and player.rect.right < WINDOWWIDTH:
            player.rect.right += MOVESPEED

        # Draw the player onto the surface.
        g.draw(screen)
        # Draw the window onto the screen.
        pygame.display.update()
        clock.tick(120)

if __name__ == "__main__":
    movements()