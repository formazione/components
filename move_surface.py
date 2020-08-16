
import pygame, sys, random
from pygame.locals import *
# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window.
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Collision Detection')


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Sprite, self).__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((10, 10))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect = self.image.get_rect()


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
        screen.blit(player.image, (player.rect.left, player.rect.top))
        # Draw the window onto the screen.
        pygame.display.update()
        mainClock.tick(120)

if __name__ == "__main__":
    movements()