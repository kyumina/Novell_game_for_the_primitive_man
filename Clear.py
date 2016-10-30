

import pygame
from pygame.locals import *
import sys

import CONSTS
import Scripts

class Clear:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1333,752))
        self.screenRect=self.screen.get_rect()
        pygame.display.set_caption(CONSTS.GAME_NAME)
        self.setSomething()
        self.draw()
        pygame.mixer.music.stop()
        self.screen=pygame.display.set_mode(CONSTS.SCREEN_SIZE)

    def setSomething(self):
        self.playbgm = Scripts.BGM("bbemybaby.mp3")
        self.playbgm.play()
        self.backimg = Scripts.BackImage("bbemyZyonir.PNG")

    def draw(self):
        while True:
            self.screen.fill((255,255,255))

            self.backimg.raw_draw(self.screen)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    return
                if event.type==QUIT:
                    sys.exit()

if __name__=="__main__":
    Clear()