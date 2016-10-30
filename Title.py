

import pygame
from pygame.locals import *
import tkinter
import tkinter.filedialog
import sys

#自作群
import CONSTS
import Scripts
import Main

class Title:
    def __init__(self):
        tkinter.Tk().withdraw()
        self.args = {"filetypes" : [("uhouhoSaveFile", "*.homo")],
        "title" : "choose save file"
        }
        pygame.init()
        self.screen=pygame.display.set_mode(CONSTS.SCREEN_SIZE)
        self.screenRect=self.screen.get_rect()
        pygame.display.set_caption(CONSTS.GAME_NAME)
        self.setWords()
        self.draw()

    def setWords(self):
        self.word_rogo1 = Scripts.Title_Button("げんしじんのための",50,(0,0,0))
        self.word_rogo1.setpos((self.screenRect.centerx-self.word_rogo1.getRect().centerx,self.screenRect.top+50))
        self.word_rogo2 = Scripts.Title_Button("Novel GAME",50,(0,0,0))
        self.word_rogo2.setpos((self.screenRect.centerx-self.word_rogo2.getRect().centerx,self.screenRect.top+self.word_rogo1.getRect().height+50))

        self.word_start = Scripts.Title_Button("はじめる",50,(0,0,0))
        self.word_start.setpos((self.screenRect.centerx-self.word_start.getRect().centerx,self.screenRect.centery+10))
        self.word_continue = Scripts.Title_Button("よみこむ",50,(0,0,0))
        self.word_continue.setpos((self.screenRect.centerx-self.word_continue.getRect().centerx,self.screenRect.centery+self.word_continue.getRect().height+10))
        self.word_finish = Scripts.Title_Button("おわる",50,(0,0,0))
        self.word_finish.setpos((self.screenRect.centerx-self.word_finish.getRect().centerx,self.screenRect.centery+self.word_start.getRect().centery+self.word_continue.getRect().centery+self.word_finish.getRect().height+10))

    def draw(self):
        while True:
            self.screen.fill((255,255,255))

            #マウスの場所を取得する
            mousepos=pygame.mouse.get_pos()
            #枠を作る
            #pygame.draw.rect(self.screen,(0,0,0),self.screenRect.inflate(-10,-10),5)
            #文字を出す
            self.word_rogo1.blit_word(self.screen)
            self.word_rogo2.blit_word(self.screen)
            self.word_start.mouseNotice(mousepos)
            self.word_start.blit_word(self.screen)
            self.word_continue.mouseNotice(mousepos)
            self.word_continue.blit_word(self.screen)
            self.word_finish.mouseNotice(mousepos)
            self.word_finish.blit_word(self.screen)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    self.word_start.mouseDownNotice(mousepos,lambda x:Main.Main(),None)
                    self.word_continue.mouseDownNotice(mousepos,lambda x:tkinter.filedialog.askopenfilename(**self.args),None)
                    self.word_finish.mouseDownNotice(mousepos,lambda x:sys.exit(),None)
                if event.type==QUIT:
                    sys.exit()


if __name__=="__main__":
    Title()