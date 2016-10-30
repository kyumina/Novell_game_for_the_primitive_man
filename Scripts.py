

import pygame
from pygame.locals import *

#ユーザ定義のライブラリ
import CONSTS

pygame.init()

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

GamemsgFont = pygame.font.Font("meiryo.ttc",CONSTS.GAME_MSG_FONT_SIZE)

class MessageAuthor:
    def __init__(self,name):
        self.name=name
        self.type="author"
        self.namesurface = pygame.Surface(CONSTS.AUTHOR_AREA_SIZE)
        self.namesurface.fill(CONSTS.AUTHOR_AREA_COLOR)
        self.blit_name()
    def blit_name(self):
        output=GamemsgFont.render(self.name,True,CONSTS.GAME_MSG_COLOR)
        self.namesurface.blit(output,CONSTS.AUTHOR_AREA_POS)
    def draw(self,screen):
        screen.blit(self.namesurface,CONSTS.AUTHOR_AREA_TOPLEFT)


class MessageWindow:
    def __init__(self,msg):
        self.type="msg"
        self.msg = msg
        self.splitmsg()
        self.msgsurface = pygame.Surface(CONSTS.MSG_AREA_SIZE)
        self.msgsurface.fill(CONSTS.MSG_AREA_COLOR)
        self.blit_msg()
    def splitmsg(self):
        self.splitedmsg=""
        count=0
        for one in self.msg:
            count+=1
            if not(count%CONSTS.GAME_MSG_SPLIT_COUNT):
                self.splitedmsg= self.splitedmsg + "\n"
            self.splitedmsg=self.splitedmsg+one
        self.msges = self.splitedmsg.splitlines()
    def blit_msg(self):
        left=CONSTS.GAME_MSG_POS[1]
        for s in self.msges:
            output=GamemsgFont.render(s,True,CONSTS.GAME_MSG_COLOR)
            self.msgsurface.blit(output,(CONSTS.GAME_MSG_POS[0],left))
            left+=CONSTS.GAME_MSG_INDENT
    def draw(self,screen):
        screen.blit(self.msgsurface,CONSTS.MSG_AREA_TOPLEFT)

class Selecter:
    def __init__(self,choiceList):
        self.type="select"
        self.choiceList=choiceList
        self.backSurface=pygame.Surface(CONSTS.SCREEN_SIZE,SRCALPHA)
        self.backSurface.fill((0,0,0,CONSTS.SELECTER_BACK_ALPHA))
        self.rectlist=[]
        self.set_surface()
    def set_surface(self):
        left=CONSTS.SELECTER_MSG_BACK_POS[1]
        for i,s in enumerate(self.choiceList):
            msgbackrect = pygame.Rect((CONSTS.SELECTER_MSG_BACK_POS[0],left),CONSTS.SELECTER_MSG_BACK_SIZE)
            pygame.draw.rect(self.backSurface,(255,255,255,CONSTS.SELECTER_MSG_BACK_ALPHA),msgbackrect)
            output=GamemsgFont.render(str(i+1)+"."+s[0],True,CONSTS.GAME_MSG_COLOR)
            self.backSurface.blit(output,msgbackrect.move(CONSTS.SELECTER_MSG_POS[0],CONSTS.SELECTER_MSG_POS[1]))
            self.rectlist.append([msgbackrect,s[1]])
            left+=CONSTS.SELECTER_MSG_BACK_INDENT
    def colision(self,pos):
        for rect in self.rectlist:
            if rect[0].collidepoint(pos):
                return rect[1]
        return None
    def draw(self,screen):
        screen.blit(self.backSurface,CONSTS.SELECTER_MSG_TOPLEFT)


class BackImage:
    def __init__(self,filename):
        self.type="back"
        self.raw_image=pygame.image.load(filename).convert()
        self.image = pygame.transform.scale(self.raw_image,CONSTS.SCREEN_SIZE)
    def draw(self,screen):
        screen.blit(self.image,(0,0))
    def raw_draw(self,screen):
        screen.blit(self.raw_image,(0,0))

class Tachie:
    def __init__(self,filename):
        self.type="tachie"
        self.image=pygame.image.load(filename).convert_alpha()
    def draw(self,screen):
        screen.blit(self.image,CONSTS.GAME_TACHIE_POS)

class BGM:
    def __init__(self,filename):
        self.type="music"
        self.filename=filename
    def play(self):
        pygame.mixer.music.load(self.filename)  # BGMをロード
        pygame.mixer.music.play(-1)  # BGMを再生

#draw出来るものの表示を消す為のclass
class NoneBOX:
    def __init__(self,type):
        self.type = type
    def draw(self,screen):
        pass #そう。まさに文字通り何もしない。


class SE:
    def __init__(self,filename):
        self.type="se"
        self.se=pygame.mixer.Sound(filename)
    def play(self):
        self.se.play()

class Scenario:
    def __init__(self,scenarioflag):
        self.scenarioflag=scenarioflag
        self.scenarioList=[]
        self.nextflag=0
    def add(self,scenarioObj):
        self.scenarioList.append(scenarioObj)
    def next(self):
        try:
            self.nextflag+=1
            return self.scenarioList[self.nextflag-1]
        except:
            return None


def Loadusf(filename):
    f = open(filename,'r',encoding="utf-8")
    ScenarioDict = dict()
    scenarioflag=""
    #TODO:objectがNoneの場合の処理を書くこと
    for line in f:
        lineparced=line[:-1].split(',')
        if (lineparced[0]=="@"):
            ScenarioDict[lineparced[1]] = Scenario(lineparced[1])
            scenarioflag=lineparced[1]
        elif (lineparced[0]=="music"):
            ScenarioDict[scenarioflag].add(BGM(lineparced[1]))
        elif (lineparced[0]=="tachie"):
            ScenarioDict[scenarioflag].add(Tachie(lineparced[1]))
        elif (lineparced[0]=="back"):
            ScenarioDict[scenarioflag].add(BackImage(lineparced[1]))
        elif (lineparced[0]=="msg"):
            ScenarioDict[scenarioflag].add(MessageAuthor(lineparced[1]))
            ScenarioDict[scenarioflag].add(MessageWindow(lineparced[2]))
        elif (lineparced[0]=="se"):
            ScenarioDict[scenarioflag].add(SE(lineparced[1]))
        elif (lineparced[0]=="select"):
            buf=[]
            result=[]
            for i,s in enumerate(lineparced[1:]):
                buf.append(s)
                if i%2:
                    result.append(buf)
                    buf=[]
            ScenarioDict[scenarioflag].add(Selecter(result))
        elif (lineparced[0]=="None"):
            ScenarioDict[scenarioflag].add(NoneBOX(lineparced[1]))
        elif (lineparced[0]=="clear"):
            ScenarioDict[scenarioflag].add("clear")
        elif (lineparced[0]=="gameover"):
            ScenarioDict[scenarioflag].add("gameover")
        else:
            pass #nop
    return ScenarioDict