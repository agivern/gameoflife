import pygame
import sys
import constant
from cell import Cell

def eventHandler():
    # Stop the game if the windows is closed
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)

def renderHandler(oScreen, aCell):
    oScreen.fill(constant.COLOR_WHITE)
    for oCell in aCell:
        oCell.render(oScreen)

def run():
    pygame.init()
    oScreen = pygame.display.set_mode(constant.RESOLUTION)
    pygame.display.set_caption('gameoflife')

    oClock = pygame.time.Clock()
    pygame.key.set_repeat(1, 1)

    aCell = list()
    aCell.append(Cell(50,50))

    while True:
        eventHandler()
        renderHandler(oScreen, aCell)

        pygame.display.flip()

        oClock.tick(constant.FPS)

if __name__ == "__main__":
    run()
