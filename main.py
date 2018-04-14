import pygame
import sys

FPS = 60
RESOLUTION = 720, 480
COLOR_BLACK = (0,0,0)

def eventHandler():
    # Stop the game if the windows is closed
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)

def run():
    pygame.init()
    oScreen = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption('gameoflife')

    oClock = pygame.time.Clock()
    pygame.key.set_repeat(1, 1)

    while True:
        eventHandler()

        oScreen.fill(COLOR_BLACK)

        pygame.display.flip()

        oClock.tick(FPS)

if __name__ == "__main__":
    run()
