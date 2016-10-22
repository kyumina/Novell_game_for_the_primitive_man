

import pygame
from pygame.locals import *

class Title_Button:
    def __init__(self,name,fontsize,color):
        self.myfont = pygame.font.Font("meiryo.ttc",fontsize)
        self.name=name
        self.color=color
        self.backcolor=(100,255,255)
        self.output = self.myfont.render(name,True,color)
    def setpos(self,pos):
        self.pos = pos
    def colision(self,pos):
        return self.output.get_rect().move(self.pos[0],self.pos[1]).collidepoint(pos)
    def getRect(self):
        return self.output.get_rect()
    def mouseNotice(self,pos):
        if (self.colision(pos)):
            self.output = self.myfont.render(self.name,True,self.color,self.backcolor)
        else:
            self.output = self.myfont.render(self.name,True,self.color)
    def mouseDownNotice(self,pos,dofunc,funcarg):
        if (self.colision(pos)):
            dofunc(funcarg)
    def blit_word(self,screen):
        screen.blit(self.output,self.pos)