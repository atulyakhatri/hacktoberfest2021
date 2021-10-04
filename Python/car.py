#IMPORTING MODULES
import pygame

pygame.init()

#Constants
GRAY = (119, 118, 110)
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

GAME_DISPLAYS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("car game")
clock = pygame.time.Clock()

def game_loop():
    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True

        GAME_DISPLAYS.fill(GRAY)
        pygame.display.update()
        clock.tick(2)

game_loop()
pygame.quit()
quit()
