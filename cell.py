import pygame
import constant

class Cell:

    def __init__(self, fPositionX, fPositionY):
        self.fPositionX = fPositionX
        self.fPositionY = fPositionY
        self.bActive = True

    def render(self, oWindow):
        pygame.draw.rect(
            oWindow,
            constant.COLOR_BLACK,
            (self.fPositionX, self.fPositionY, 32, 32)
        )
