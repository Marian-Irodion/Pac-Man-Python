import pygame, sys
from button import Button
import random
from pygame.locals import *
from pygame import mixer
import time

pygame.init()

clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((1400, 700))
pygame.display.set_caption("Menu")

global global_score
global_score = 0

BG = pygame.image.load("final frame.png")
coinImage = pygame.image.load("coin.png")

mixer.init()
background = pygame.mixer.Sound('level2.ogg')
buttonel = pygame.mixer.Sound('button.ogg')
buttonel.set_volume(1.0)
background.set_volume(0.5)
nivelas1 = pygame.mixer.Sound('oh_yeah.ogg')
nivelas2 = pygame.mixer.Sound('facetoface.ogg')
nivelas3 = pygame.mixer.Sound('aroundtheworld.ogg')
nivelas3.set_volume(0.7)
nivelas2.set_volume(0.7)
nivelas1.set_volume(0.7)
pac_dead = pygame.mixer.Sound('pacdead.ogg')
pac_kill = pygame.mixer.Sound('packill.ogg')
pac_stronk = pygame.mixer.Sound('pacpowerup.ogg')
pac_dead.set_volume(1)
pac_kill.set_volume(1)
pac_stronk.set_volume(1)

global replay
replay = 0

cell_width = 40
cell_height = 40

lines = 35
columns = 55

global psx
global psy

#background.play(0)

class Coins(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.transform.scale(coinImage, (7, 7))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

class Walls(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("block.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

class Phanto1(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("fantored-Recovered.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.possx = pos_x
        self.possy = pos_y
        self.weak = False

        def update(self):
            self.rect.topleft = [self.possx, self.possy]

        def gety(self, n_x, n_y):
            self.possx += n_x
            self.possy += n_y

class Phanto2(pygame.sprite.Sprite):
    def __init__(selfii, pos_x, pos_y):
        super().__init__()
        selfii.image = pygame.image.load("fantopink.png")
        selfii.image = pygame.transform.scale(selfii.image, (20, 20))
        selfii.rect = selfii.image.get_rect()
        selfii.rect.topleft = [pos_x, pos_y]
        selfii.possx = pos_x
        selfii.possy = pos_y
        selfii.weak = False

        def update(selfii):
            selfii.rect.topleft = [selfii.possx, selfii.possy]

        def getty(selfii, n_x, n_y):
            selfii.possx += n_x
            selfii.possy += n_y

class Phanto3(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("fantoyell.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.possx = pos_x
        self.possy = pos_y
        self.weak = False

        def update(self):
            self.rect.topleft = [self.possx, self.possy]

        def gettty(self, n_x, n_y):
            self.possx += n_x
            self.possy += n_y

class Phanto4(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("fantoturq.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.possx = pos_x
        self.possy = pos_y
        self.weak = False

        def update(self):
            self.rect.topleft = [self.possx, self.possy]

        def getttty(self, n_x, n_y):
            self.possx += n_x
            self.possy += n_y


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("powerup1.png")
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.respawn = False



class Coins2(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.transform.scale(coinImage, (13, 13))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

class Walls2(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("block.png")
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

class Phanto1_2(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("fantored-Recovered.png")
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.possx = pos_x
        self.possy = pos_y
        self.weak = False

        def update(self):
            self.rect.topleft = [self.possx, self.possy]

        def gety(self, n_x, n_y):
            self.possx += n_x
            self.possy += n_y

class Phanto2_2(pygame.sprite.Sprite):
    def __init__(selfii, pos_x, pos_y):
        super().__init__()
        selfii.image = pygame.image.load("fantopink.png")
        selfii.image = pygame.transform.scale(selfii.image, (25, 25))
        selfii.rect = selfii.image.get_rect()
        selfii.rect.topleft = [pos_x, pos_y]
        selfii.possx = pos_x
        selfii.possy = pos_y
        selfii.weak = False

        def update(selfii):
            selfii.rect.topleft = [selfii.possx, selfii.possy]

        def getty(selfii, n_x, n_y):
            selfii.possx += n_x
            selfii.possy += n_y

class Phanto3_2(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("fantoyell.png")
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.possx = pos_x
        self.possy = pos_y
        self.weak = False

        def update(self):
            self.rect.topleft = [self.possx, self.possy]

        def gettty(self, n_x, n_y):
            self.possx += n_x
            self.possy += n_y

class Phanto4_2(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("fantoturq.png")
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.possx = pos_x
        self.possy = pos_y
        self.weak = False

        def update(self):
            self.rect.topleft = [self.possx, self.possy]

        def getttty(self, n_x, n_y):
            self.possx += n_x
            self.possy += n_y


class PowerUp2(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("powerup1.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.respawn = False


class Coins3(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.transform.scale(coinImage, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

class Walls3(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("block.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

class Phanto1_3(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("fantored-Recovered.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.possx = pos_x
        self.possy = pos_y
        self.weak = False

        def update(self):
            self.rect.topleft = [self.possx, self.possy]

        def gety(self, n_x, n_y):
            self.possx += n_x
            self.possy += n_y

class Phanto2_3(pygame.sprite.Sprite):
    def __init__(selfii, pos_x, pos_y):
        super().__init__()
        selfii.image = pygame.image.load("fantopink.png")
        selfii.image = pygame.transform.scale(selfii.image, (50, 50))
        selfii.rect = selfii.image.get_rect()
        selfii.rect.topleft = [pos_x, pos_y]
        selfii.possx = pos_x
        selfii.possy = pos_y
        selfii.weak = False

        def update(selfii):
            selfii.rect.topleft = [selfii.possx, selfii.possy]

        def getty(selfii, n_x, n_y):
            selfii.possx += n_x
            selfii.possy += n_y

class Phanto3_3(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("fantoyell.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.possx = pos_x
        self.possy = pos_y
        self.weak = False

        def update(self):
            self.rect.topleft = [self.possx, self.possy]

        def gettty(self, n_x, n_y):
            self.possx += n_x
            self.possy += n_y

class Phanto4_3(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("fantoturq.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.possx = pos_x
        self.possy = pos_y
        self.weak = False

        def update(self):
            self.rect.topleft = [self.possx, self.possy]

        def getttty(self, n_x, n_y):
            self.possx += n_x
            self.possy += n_y


class PowerUp3(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("powerup1.png")
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.respawn = False


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

def main_menu():
    if replay == 1:
        background.play(0)
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=None, pos=(700, 550),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="magenta")
        HIGH_SCORE_BUTTON = Button(image=None, pos=(245, 425),
                                text_input="INFO", font=get_font(75), base_color="#d7fcd4", hovering_color="magenta")
        QUIT_BUTTON = Button(image=None, pos=(1150, 425),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="magenta")

        for button in [PLAY_BUTTON, HIGH_SCORE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    play()
                if HIGH_SCORE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    high_score()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def play():
    nivelas3.stop()
    nivelas2.stop()
    nivelas1.stop()
    #global_score = 0
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY = pygame.image.load("listf.png")
        PLAY = pygame.transform.scale(PLAY, (1400, 700))
        SCREEN.blit(PLAY, (0, 0))

        PLAY_BACK = Button(image=None, pos=(640, 625),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="magenta")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        PLAY_1 = Button(image=None, pos=(765, 85),
                           text_input="Oh, yeah! Come here!", font=get_font(50), base_color="White", hovering_color="magenta")

        PLAY_1.changeColor(PLAY_MOUSE_POS)
        PLAY_1.update(SCREEN)

        PLAY_2 = Button(image=None, pos=(765, 285),
                           text_input="Face to Face", font=get_font(50), base_color="White", hovering_color="magenta")

        PLAY_2.changeColor(PLAY_MOUSE_POS)
        PLAY_2.update(SCREEN)

        PLAY_3 = Button(image=None, pos=(765, 485),
                           text_input="Around the world", font=get_font(50), base_color="White", hovering_color="magenta")

        PLAY_3.changeColor(PLAY_MOUSE_POS)
        PLAY_3.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    main_menu()
                if PLAY_1.checkForInput(PLAY_MOUSE_POS):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    level_2()
                if PLAY_2.checkForInput(PLAY_MOUSE_POS):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    level_1()
                if PLAY_3.checkForInput(PLAY_MOUSE_POS):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    level_3()

        pygame.display.update()

def high_score():
    while True:
        HIGH_SCORE_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        SCORES=pygame.image.load("top.png")
        SCORES=pygame.transform.scale(SCORES, (1400, 700))
        SCREEN.blit(SCORES, (0, 0))

        OPTIONS_BACK = Button(image=None, pos=(1175, 650),
                              text_input="BACK", font=get_font(50), base_color="green", hovering_color="magenta")

        OPTIONS_BACK.changeColor(HIGH_SCORE_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        GENERAL = Button(image=None, pos=(235, 165),
                              text_input="NOTRE AMI: PAC", font=get_font(15), base_color="black", hovering_color="magenta")

        GENERAL.changeColor(HIGH_SCORE_MOUSE_POS)
        GENERAL.update(SCREEN)

        GEN_BR = Button(image=None, pos=(700, 165),
                              text_input="MANDRIA", font=get_font(20), base_color="black", hovering_color="magenta")

        GEN_BR.changeColor(HIGH_SCORE_MOUSE_POS)
        GEN_BR.update(SCREEN)

        COLONEL = Button(image=None, pos=(1175, 165),
                              text_input="BANII", font=get_font(20), base_color="black", hovering_color="magenta")

        COLONEL.changeColor(HIGH_SCORE_MOUSE_POS)
        COLONEL.update(SCREEN)

        LT_COL = Button(image=None, pos=(235, 395),
                              text_input="BLINKY", font=get_font(20), base_color="black", hovering_color="magenta")

        LT_COL.changeColor(HIGH_SCORE_MOUSE_POS)
        LT_COL.update(SCREEN)

        MAIOR = Button(image=None, pos=(700, 395),
                              text_input="PINKY", font=get_font(20), base_color="black", hovering_color="magenta")

        MAIOR.changeColor(HIGH_SCORE_MOUSE_POS)
        MAIOR.update(SCREEN)

        CAPITAN = Button(image=None, pos=(1175, 395),
                              text_input="INKY", font=get_font(20), base_color="black", hovering_color="magenta")

        CAPITAN.changeColor(HIGH_SCORE_MOUSE_POS)
        CAPITAN.update(SCREEN)

        LOCOTENENT = Button(image=None, pos=(235, 630),
                              text_input="CLYDE", font=get_font(20), base_color="black", hovering_color="magenta")

        LOCOTENENT.changeColor(HIGH_SCORE_MOUSE_POS)
        LOCOTENENT.update(SCREEN)

        SGP = Button(image=None, pos=(700, 630),
                              text_input="GAMEPLAY", font=get_font(20), base_color="black", hovering_color="magenta")

        SGP.changeColor(HIGH_SCORE_MOUSE_POS)
        SGP.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(HIGH_SCORE_MOUSE_POS):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    main_menu()
                if SGP.checkForInput(HIGH_SCORE_MOUSE_POS):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    options()
                if LOCOTENENT.checkForInput(HIGH_SCORE_MOUSE_POS):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    clyde()
                if CAPITAN.checkForInput(HIGH_SCORE_MOUSE_POS):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    inky()
                if MAIOR.checkForInput(HIGH_SCORE_MOUSE_POS):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    pinky()
                if LT_COL.checkForInput(HIGH_SCORE_MOUSE_POS):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    blinky()
                if COLONEL.checkForInput(HIGH_SCORE_MOUSE_POS):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    banii()
                if GEN_BR.checkForInput(HIGH_SCORE_MOUSE_POS):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    mandria()
                if GENERAL.checkForInput(HIGH_SCORE_MOUSE_POS):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    notre_ami()

        pygame.display.update()

def inky():
    while True:
        mouse = pygame.mouse.get_pos()

        SCREEN.fill("black")

        INFO_BACK = Button(image=None, pos=(1175, 650),
                              text_input="BACK", font=get_font(50), base_color="white", hovering_color="red")

        INFO_BACK.changeColor(mouse)
        INFO_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INFO_BACK.checkForInput(mouse):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    high_score()
        font = get_font(25)
        text = font.render('Kimagure - Fickle', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 100)
        SCREEN.blit(text, textRect)
        text = font.render('Aosuke - Blue guy', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 200)
        SCREEN.blit(text, textRect)
        text = font.render('Stylist', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 300)
        SCREEN.blit(text, textRect)
        text = font.render('Mucky', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 400)
        SCREEN.blit(text, textRect)
        text = font.render('Bashful', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 500)
        SCREEN.blit(text, textRect)
        pygame.display.update()

def pinky():
    while True:
        mouse = pygame.mouse.get_pos()

        SCREEN.fill("black")

        INFO_BACK = Button(image=None, pos=(1175, 650),
                           text_input="BACK", font=get_font(50), base_color="white", hovering_color="red")

        INFO_BACK.changeColor(mouse)
        INFO_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INFO_BACK.checkForInput(mouse):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    high_score()
        font = get_font(25)
        text = font.render('Machibuse - Ambusher', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 100)
        SCREEN.blit(text, textRect)
        text = font.render('Pinkī - Pinky', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 200)
        SCREEN.blit(text, textRect)
        text = font.render('Romp', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 300)
        SCREEN.blit(text, textRect)
        text = font.render('Micky', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 400)
        SCREEN.blit(text, textRect)
        text = font.render('Speedy', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 500)
        SCREEN.blit(text, textRect)
        pygame.display.update()

def blinky():
    while True:
        mouse = pygame.mouse.get_pos()

        SCREEN.fill("black")

        INFO_BACK = Button(image=None, pos=(1175, 650),
                           text_input="BACK", font=get_font(50), base_color="white", hovering_color="red")

        INFO_BACK.changeColor(mouse)
        INFO_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INFO_BACK.checkForInput(mouse):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    high_score()
        font = get_font(25)
        text = font.render('Oikake - Chaser', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 100)
        SCREEN.blit(text, textRect)
        text = font.render('Akabei - Red guy', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 200)
        SCREEN.blit(text, textRect)
        text = font.render('Urchin', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 300)
        SCREEN.blit(text, textRect)
        text = font.render('Macky', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 400)
        SCREEN.blit(text, textRect)
        text = font.render('Shadow', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 500)
        SCREEN.blit(text, textRect)
        pygame.display.update()

def clyde():
    while True:
        mouse = pygame.mouse.get_pos()

        SCREEN.fill("black")

        INFO_BACK = Button(image=None, pos=(1175, 650),
                           text_input="BACK", font=get_font(50), base_color="white", hovering_color="red")

        INFO_BACK.changeColor(mouse)
        INFO_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INFO_BACK.checkForInput(mouse):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    high_score()
        font = get_font(25)
        text = font.render('Otoboke - Feigned Ignorance', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 100)
        SCREEN.blit(text, textRect)
        text = font.render('Guzuta - Slow guy', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 200)
        SCREEN.blit(text, textRect)
        text = font.render('Crybaby', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 300)
        SCREEN.blit(text, textRect)
        text = font.render('Mocky', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 400)
        SCREEN.blit(text, textRect)
        text = font.render('Pokey', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 500)
        SCREEN.blit(text, textRect)
        pygame.display.update()

def options():
    while True:
        mouse = pygame.mouse.get_pos()

        SCREEN.fill("black")

        INFO_BACK = Button(image=None, pos=(1175, 650),
                           text_input="BACK", font=get_font(50), base_color="white", hovering_color="red")

        INFO_BACK.changeColor(mouse)
        INFO_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INFO_BACK.checkForInput(mouse):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    high_score()
        font = get_font(30)
        text = font.render('Useful information: ', True, "red", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 50)
        SCREEN.blit(text, textRect)
        font = get_font(20)
        text = font.render('-deplasare: sagetile tastaturii', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 150)
        SCREEN.blit(text, textRect)
        text = font.render('-dispui, la fiecare nivel, de cate 3 vieti', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 250)
        SCREEN.blit(text, textRect)
        text = font.render('-prinderea unui pachet de tigari iti da posibilitatea,', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 350)
        SCREEN.blit(text, textRect)
        text = font.render('pentru urmatoarele 5 secunde, sa mananci o fantoma', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 450)
        SCREEN.blit(text, textRect)
        text = font.render('-poti pune pauza de pe tasta <<ESC>>, iar reluarea de pe <<SPACE>>', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 550)
        SCREEN.blit(text, textRect)
        pygame.display.update()

def mandria():
    while True:
        mouse = pygame.mouse.get_pos()

        SCREEN.fill("black")

        INFO_BACK = Button(image=None, pos=(1175, 650),
                           text_input="BACK", font=get_font(50), base_color="white", hovering_color="red")

        INFO_BACK.changeColor(mouse)
        INFO_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INFO_BACK.checkForInput(mouse):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    high_score()
        font = get_font(25)
        text = font.render('Dupa power-up crezi ca esti invincibil,', True, "white", "black")
        text2 = font.render('dar de fapt te vei adanci si mai tare in pierzanie!', True, "white", "black")
        textRect = text.get_rect()
        textRect2 = text2.get_rect()
        textRect.center = (1400 // 2, 250)
        textRect2.center = (1400 // 2, 350)
        SCREEN.blit(text, textRect)
        SCREEN.blit(text2, textRect2)
        pygame.display.update()

def banii():
    while True:
        mouse = pygame.mouse.get_pos()

        SCREEN.fill("black")

        INFO_BACK = Button(image=None, pos=(1175, 650),
                           text_input="BACK", font=get_font(50), base_color="white", hovering_color="red")

        INFO_BACK.changeColor(mouse)
        INFO_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INFO_BACK.checkForInput(mouse):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    high_score()
        font = get_font(25)
        text = font.render('Degeaba strangi banutii de la toate nivelele,', True, "white", "black")
        text2 = font.render('oricum la un moment dat vei muri!', True, "white", "black")
        textRect = text.get_rect()
        textRect2 = text2.get_rect()
        textRect.center = (1400 // 2, 250)
        textRect2.center = (1400 // 2, 350)
        SCREEN.blit(text, textRect)
        SCREEN.blit(text2, textRect2)
        pygame.display.update()

def notre_ami():
    while True:
        mouse = pygame.mouse.get_pos()

        SCREEN.fill("black")

        INFO_BACK = Button(image=None, pos=(1175, 650),
                           text_input="BACK", font=get_font(50), base_color="white", hovering_color="red")

        INFO_BACK.changeColor(mouse)
        INFO_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INFO_BACK.checkForInput(mouse):
                    buttonel.set_volume(1.0)
                    buttonel.play(0)
                    high_score()
        font = get_font(15)
        text = font.render('Scopul este sa fure toti banii incercand', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 100)
        SCREEN.blit(text, textRect)
        text = font.render('in acelasi timp sa nu fie prins de fantome.', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 200)
        SCREEN.blit(text, textRect)
        text = font.render('Pentru puncte bonus, pachetele de tigari care apar pot fi de asemenea mancate.', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 300)
        SCREEN.blit(text, textRect)
        text = font.render('Cand Pac-Man fumeaza pachetul,', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 400)
        SCREEN.blit(text, textRect)
        text = font.render('fantomele capata culoarea albastra si pot fi servite pentru si mai multe puncte.', True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (1400 // 2, 500)
        SCREEN.blit(text, textRect)
        pygame.display.update()


def level_3():
    background.stop()
    #-----------GENERAL ASSETS-----------
    nivelas3.play(0)
    pause = False
    speed = 1

    LEVEL_1 = pygame.mouse.get_pos()

    pacman_group = pygame.sprite.Group()

    coins_group = pygame.sprite.Group()

    walls_group = pygame.sprite.Group()

    powerup_group = pygame.sprite.Group()

    phanto1_group = pygame.sprite.Group()
    phanto2_group = pygame.sprite.Group()
    phanto3_group = pygame.sprite.Group()
    phanto4_group = pygame.sprite.Group()

    #---------------MAP READING----------

    file = open('walls.txt', 'r')
    bx = 0
    by = 0

    font = pygame.font.SysFont('Consolas', 30)

    f1x = 0
    f1y = 0
    f2x = 0
    f2y = 0
    f3x = 0
    f3y = 0
    f4x = 0
    f4y = 0

    while 1:

        char = file.read(1)
        if not char:
            break
        if char == "0":
            new_coin = Coins(by * 20, bx * 20)
            coins_group.add(new_coin)
        if char == "1":
            new_wall = Walls(by * 20, bx * 20)
            walls_group.add(new_wall)
        if char == "4":
            new_power = PowerUp(by * 20, bx * 20)
            powerup_group.add(new_power)
        if char == "5":
            f1x = by*20
            f1y = bx*20
        if char == "6":
            f2x = by * 20
            f2y = bx * 20
        if char == "7":
            f3x = by * 20
            f3y = bx * 20
        if char == "9":
            psx = by * 20
            psy = bx * 20
        if char == "8":
            f4x = by * 20
            f4y = bx * 20
        if by >= 55:
            by = 0
            bx = bx + 1
        else:
            by = by + 1

    file.close()

    #---------------PLAYER DEFINITION------------

    class Pacman(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            super().__init__()
            self.pacman_dx = psx
            self.pacman_dy = psy
            self.image = pygame.image.load("high.png")
            self.image = pygame.transform.scale(self.image, (15, 15))
            self.rect = self.image.get_rect()
            self.rect.topleft = [pos_x, pos_y]
            self.test = None
            self.lives = 3
            self.score = 0

        def update(self):
            self.rect.topleft = [self.pacman_dx, self.pacman_dy]

        def collisions(self):
            coll = pygame.sprite.spritecollide(pacman, coins_group, True, pygame.sprite.collide_rect)
            if coll:
                self.score += 1


        def get_position(self, n_x, n_y):
            self.pacman_dx += n_x
            self.pacman_dy += n_y

    pacman = Pacman(0, 0)
    pacman_group.add(pacman)

    #----------GHOSTS SET UP---------

    reset1x = f1x
    reset1y = f1y
    reset2x = f2x
    reset2y = f2y
    reset3x = f3x
    reset3y = f3y
    reset4x = f4x
    reset4y = f4y

    fanto1 = Phanto1(f1x, f1y)
    fanto2 = Phanto2(f2x, f2y)
    fanto3 = Phanto3(f3x, f3y)
    fanto4 = Phanto4(f4x, f4y)

    phanto1_group.add(fanto1)
    phanto2_group.add(fanto2)
    phanto3_group.add(fanto3)
    phanto4_group.add(fanto4)

    #------------SPEED SET UP---------

    global velocity
    velocity = (0, 0)
    global old_velocity
    old_velocity = velocity

    global p1velocity
    global p2velocity
    global p3velocity
    global p4velocity

    p1velocity = (0, 0)
    p2velocity = (0, 0)
    p3velocity = (0, 0)
    p4velocity = (0, 0)

    oldv1 = p1velocity
    oldv2 = p2velocity
    oldv3 = p3velocity
    oldv4 = p4velocity

    #----------------HUNTER TIMER----------

    global ticker
    ticker = 0

    #--------------LEVEL 1 GAME LOOP----------+

    while True:
        status = "PREY"
        checker = len(coins_group.sprites())
        #victoria

        #----------SPEEED UPDATER---------------
        ok = 1
        pacman.get_position(velocity[0], velocity[1])
        oldv1 = p1velocity
        oldv2 = p2velocity
        oldv3 = p3velocity
        oldv4 = p4velocity
        f1x += p1velocity[0]
        f2x += p2velocity[0]
        f3x += p3velocity[0]
        f4x += p4velocity[0]
        f1y += p1velocity[1]
        f2y += p2velocity[1]
        f3y += p3velocity[1]
        f4y += p4velocity[1]
        fanto1.rect.topleft = [f1x, f1y]
        fanto2.rect.topleft = [f2x, f2y]
        fanto3.rect.topleft = [f3x, f3y]
        fanto4.rect.topleft = [f4x, f4y]

        pressedKeys = pygame.key.get_pressed()

        #------------GETTING EVENTS-----------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pacman.collisions()

        #----------DECREASE/INCREASE SPEED--------

        if pressedKeys[pygame.K_c]:
            speed = 1

        if pressedKeys[pygame.K_v]:
            speed = 2

        if pressedKeys[pygame.K_b]:
            speed = 3

        if pressedKeys[pygame.K_ESCAPE]:
            pause = True
        if pressedKeys[pygame.K_SPACE]:
            pause = False

        #-------------GHOSTS DIRECTIONS------

        validator = 0
        validator = random.randint(1, 10)
        if validator == 1:
            hasher = 0
            uno = (0, -2*speed)
            dos = (0, 2*speed)
            tres = (2*speed, 0)
            quatro = (-2*speed, 0)
            hasher = random.randint(1, 4)
            if hasher == 1:
                p1velocity = uno
            if hasher == 2:
                p1velocity = dos
            if hasher == 3:
                p1velocity = tres
            if hasher == 4:
                p1velocity = quatro
            hasher = random.randint(1, 4)
            if hasher == 1:
                p2velocity = uno
            if hasher == 2:
                p2velocity = dos
            if hasher == 3:
                p2velocity = tres
            if hasher == 4:
                p2velocity = quatro
            hasher = random.randint(1, 4)
            if hasher == 1:
                p3velocity = uno
            if hasher == 2:
                p3velocity = dos
            if hasher == 3:
                p3velocity = tres
            if hasher == 4:
                p3velocity = quatro
            hasher = random.randint(1, 4)
            if hasher == 1:
                p4velocity = uno
            if hasher == 2:
                p4velocity = dos
            if hasher == 3:
                p4velocity = tres
            if hasher == 4:
                p4velocity = quatro

        #-----------GHOSTS COLLISIIONS-----------

        collf1 = pygame.sprite.spritecollide(fanto1, walls_group, False, pygame.sprite.collide_rect)
        collf2 = pygame.sprite.spritecollide(fanto2, walls_group, False, pygame.sprite.collide_rect)
        collf3 = pygame.sprite.spritecollide(fanto3, walls_group, False, pygame.sprite.collide_rect)
        collf4 = pygame.sprite.spritecollide(fanto4, walls_group, False, pygame.sprite.collide_rect)

        if collf1:
            f1x -=oldv1[0]
            f1y -=oldv1[1]

        if collf2:
            f2x -= oldv2[0]
            f2y -= oldv2[1]

        if collf3:
            f3x -= oldv3[0]
            f3y -= oldv3[1]

        if collf4:
            f4x -= oldv4[0]
            f4y -= oldv4[1]

        #-----------EATING SOBRANIE----------

        colli = pygame.sprite.spritecollide(pacman, powerup_group, True, pygame.sprite.collide_rect)
        if colli:
            pac_stronk.play()
            pacman.score += 10
            new_power.respawn = True
            ticker = 300
            if new_power.respawn:
                ok = 1
                while ok == 1:
                    pow_x = random.randint(1, 33)
                    pow_y = random.randint(1, 53)
                    new_power = PowerUp(pow_y * 20, pow_x * 20)
                    powerup_group.add(new_power)
                    colio = pygame.sprite.spritecollide(new_power, walls_group, False, pygame.sprite.collide_rect)
                    col1 = pygame.sprite.spritecollide(new_power, phanto1_group, False, pygame.sprite.collide_rect)
                    col2 = pygame.sprite.spritecollide(new_power, phanto2_group, False, pygame.sprite.collide_rect)
                    col3 = pygame.sprite.spritecollide(new_power, phanto3_group, False, pygame.sprite.collide_rect)
                    col4 = pygame.sprite.spritecollide(new_power, phanto4_group, False, pygame.sprite.collide_rect)
                    ok = 0
                    new_power.respawn = False
                    if colio or col1 or col2 or col3 or col4:
                        ok = 1
                        powerup_group.remove(new_power)

        #----------------HUNTING GHOSTS------------

        if ticker > 0:
            fanto1.weak = True
            fanto2.weak = True
            fanto3.weak = True
            fanto4.weak = True
            fanto1.image = pygame.image.load("scared.png")
            fanto1.image = pygame.transform.scale(fanto1.image, (20, 20))
            fanto2.image = pygame.image.load("scared.png")
            fanto2.image = pygame.transform.scale(fanto2.image, (20, 20))
            fanto3.image = pygame.image.load("scared.png")
            fanto3.image = pygame.transform.scale(fanto3.image, (20, 20))
            fanto4.image = pygame.image.load("scared.png")
            fanto4.image = pygame.transform.scale(fanto4.image, (20, 20))
            esc1 = False
            esc2 = False
            esc3 = False
            esc4 = False
            esc1 = pygame.sprite.spritecollide(pacman, phanto1_group, True, pygame.sprite.collide_rect)
            esc2 = pygame.sprite.spritecollide(pacman, phanto2_group, True, pygame.sprite.collide_rect)
            esc3 = pygame.sprite.spritecollide(pacman, phanto3_group, True, pygame.sprite.collide_rect)
            esc4 = pygame.sprite.spritecollide(pacman, phanto4_group, True, pygame.sprite.collide_rect)

            if esc1:
                pacman.score += 25
                f1x = reset1x
                f1y = reset1y
                fanto1 = Phanto1(f1x, f1y)
                phanto1_group.add(fanto1)
                ticker = 0
                pac_kill.play()

            if esc2:
                pacman.score += 25
                f2x = reset2x
                f2y = reset2y
                fanto2 = Phanto2(f2x, f2y)
                phanto2_group.add(fanto2)
                ticker = 0
                pac_kill.play()

            if esc3:
                pacman.score += 25
                f3x = reset3x
                f3y = reset3y
                fanto3 = Phanto3(f3x, f3y)
                phanto3_group.add(fanto3)
                ticker = 0
                pac_kill.play()

            if esc4:
                pacman.score += 25
                f4x = reset4x
                f4y = reset4y
                fanto4 = Phanto4(f4x, f4y)
                phanto4_group.add(fanto4)
                ticker = 0
                pac_kill.play()

            ticker -= 1
            status = "HUNTER"
        else:
            fanto1.weak = False
            fanto2.weak = False
            fanto3.weak = False
            fanto4.weak = False
            fanto1.image = pygame.image.load("fantored-Recovered.png")
            fanto1.image = pygame.transform.scale(fanto1.image, (20, 20))
            fanto2.image = pygame.image.load("fantopink.png")
            fanto2.image = pygame.transform.scale(fanto2.image, (20, 20))
            fanto3.image = pygame.image.load("fantoyell.png")
            fanto3.image = pygame.transform.scale(fanto3.image, (20, 20))
            fanto4.image = pygame.image.load("fantoturq.png")
            fanto4.image = pygame.transform.scale(fanto4.image, (20, 20))
            status = "PREY"

        #------------------PACMAN COLLISIONS------------

        collw = pygame.sprite.spritecollide(pacman, walls_group, False, pygame.sprite.collide_rect)

        if collw:
            velocity = old_velocity
            pacman.pacman_dy -= old_velocity[1]
            pacman.pacman_dx -= old_velocity[0]
        pacman.collisions()
        pacman_group.update()

        collw1 = pygame.sprite.spritecollide(pacman, phanto1_group, False, pygame.sprite.collide_rect)
        collw2 = pygame.sprite.spritecollide(pacman, phanto2_group, False, pygame.sprite.collide_rect)
        collw3 = pygame.sprite.spritecollide(pacman, phanto3_group, False, pygame.sprite.collide_rect)
        collw4 = pygame.sprite.spritecollide(pacman, phanto4_group, False, pygame.sprite.collide_rect)

        if (collw1 and fanto1.weak == False) or (collw2 and fanto2.weak == False) or (collw3 and fanto3.weak == False) or (collw4 and fanto4.weak == False):
            pacman.lives -= 1
            pac_dead.play()
            if pacman.lives < 1:
                nivelas3.stop()
                gameover = pygame.image.load("gameoverwoo.png")
                gameover = pygame.transform.scale(gameover, (1400, 700))
                SCREEN.blit(gameover, (0, 0))
                pygame.display.update()
                clock.tick(60)
                time.sleep(3)
                SCREEN.fill("black")
                APHISH = Button(image=None, pos=(700, 250),
                                text_input="YOUR SCORE:", font=get_font(50), base_color="yellow", hovering_color="magenta")
                APHISH.changeColor(LEVEL_1)
                APHISH.update(SCREEN)
                SCORE = Button(image=None, pos=(700, 350),
                               text_input=string, font=get_font(50), base_color="yellow", hovering_color="magenta")
                SCORE.changeColor(LEVEL_1)
                SCORE.update(SCREEN)
                pygame.display.update()
                time.sleep(2)
                main_menu()
            time.sleep(1)
            pacman.pacman_dx = psx
            pacman.pacman_dy = psy

        #----------GETTING DIRECTIONS FORM PACMAN--------------

        if ok == 1:
            if pressedKeys[pygame.K_DOWN]:
                old_velocity = velocity
                velocity = (0, 1.5*speed)
                ok = 0
        if ok == 1:
            if pressedKeys[pygame.K_UP]:
                old_velocity = velocity
                velocity = (0, -1.5*speed)
                ok = 0
        if ok == 1:
            if pressedKeys[pygame.K_RIGHT]:
                old_velocity = velocity
                velocity = (1.5*speed, 0)
                ok = 0
        if ok == 1:
            if pressedKeys[pygame.K_LEFT]:
                old_velocity = velocity
                velocity = (-1.5*speed, 0)
                ok = 0

        if checker == 0:
            #global_score += pacman.score
            walls_group.empty()
            powerup_group.empty()
            phanto1_group.empty()
            phanto2_group.empty()
            phanto3_group.empty()
            phanto4_group.empty()
            pacman_group.empty()
            string = str(pacman.score)
            APHISH = Button(image=None, pos=(700, 250),
                            text_input="FINAL SCORE:", font=get_font(50), base_color="yellow", hovering_color="magenta")
            APHISH.changeColor(LEVEL_1)
            APHISH.update(SCREEN)
            SCORE = Button(image=None, pos=(700, 350),
                           text_input=string, font=get_font(50), base_color="yellow", hovering_color="magenta")
            SCORE.changeColor(LEVEL_1)
            SCORE.update(SCREEN)
            pygame.display.update()
            time.sleep(2)
            main_menu()

        #---------GAME PAUSED/NOT PAUSED AND UPDATING THE SCREEN WITH THE PREVIOUS EVENTS----------

        if not pause:
            SCREEN.fill('black')
            string = str(pacman.score)
            ss = str(pacman.lives)
            APHISH = Button(image=None, pos=(1240, 100),
                           text_input = "SCORE", font=get_font(20), base_color="yellow", hovering_color="magenta")
            APHISH.changeColor(LEVEL_1)
            APHISH.update(SCREEN)
            SCORE = Button(image=None, pos=(1240, 150),
                           text_input = string, font=get_font(20), base_color="yellow", hovering_color="magenta")
            SCORE.changeColor(LEVEL_1)
            SCORE.update(SCREEN)
            LIVES = Button(image=None, pos=(1250, 250),
                           text_input= "REMAINED LIVES", font=get_font(20), base_color="yellow", hovering_color="magenta")
            LIVES.changeColor(LEVEL_1)
            LIVES.update(SCREEN)
            NRL = Button(image=None, pos=(1245, 300),
                           text_input=ss, font=get_font(20), base_color="yellow", hovering_color="magenta")
            NRL.changeColor(LEVEL_1)
            NRL.update(SCREEN)
            STATUS = Button(image=None, pos=(1254, 450),
                           text_input="STATUS:", font=get_font(20), base_color="yellow",
                           hovering_color="magenta")
            STATUS.changeColor(LEVEL_1)
            STATUS.update(SCREEN)
            PH = Button(image=None, pos=(1245, 500),
                         text_input=status, font=get_font(20), base_color="yellow", hovering_color="magenta")
            PH.changeColor(LEVEL_1)
            PH.update(SCREEN)
            LEVEL_1 = pygame.mouse.get_pos()
            PLAY_BACK = Button(image=None, pos=(1245, 625),
                               text_input="BACK", font=get_font(75), base_color="White", hovering_color="magenta")

            PLAY_BACK.changeColor(LEVEL_1)
            PLAY_BACK.update(SCREEN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(LEVEL_1):
                        buttonel.set_volume(1.0)
                        buttonel.play(0)
                        play()
            coins_group.draw(SCREEN)
            walls_group.draw(SCREEN)
            powerup_group.draw(SCREEN)
            phanto1_group.draw(SCREEN)
            phanto2_group.draw(SCREEN)
            phanto3_group.draw(SCREEN)
            phanto4_group.draw(SCREEN)
            pacman_group.draw(SCREEN)
            phanto1_group.update()
            phanto2_group.update()
            phanto3_group.update()
            phanto4_group.update()
            pacman_group.update()
            pygame.display.update()
            clock.tick(60)
        else:
            velocity = (0, 0)
            p1velocity = (0, 0)
            p2velocity = (0, 0)
            p3velocity = (0, 0)
            p4velocity = (0, 0)

def level_2():
    background.stop()
    # -----------GENERAL ASSETS-----------
    nivelas1.play(5)
    pause = False
    speed = 1

    LEVEL_1 = pygame.mouse.get_pos()

    pacman_group3 = pygame.sprite.Group()

    coins_group3 = pygame.sprite.Group()

    walls_group3 = pygame.sprite.Group()

    powerup_group3 = pygame.sprite.Group()

    phanto1_group3 = pygame.sprite.Group()
    phanto2_group3 = pygame.sprite.Group()
    phanto3_group3 = pygame.sprite.Group()
    phanto4_group3 = pygame.sprite.Group()

    # ---------------MAP READING----------

    file = open('walls3.txt', 'r')
    bx = 0
    by = 0

    font = pygame.font.SysFont('Consolas', 30)

    f1x = 0
    f1y = 0
    f2x = 0
    f2y = 0
    f3x = 0
    f3y = 0
    f4x = 0
    f4y = 0

    while 1:

        char = file.read(1)
        if not char:
            break
        if char == "0":
            new_coin = Coins3(by * 50, bx * 50)
            coins_group3.add(new_coin)
        if char == "1":
            new_wall = Walls3(by * 50, bx * 50)
            walls_group3.add(new_wall)
        if char == "4":
            new_power = PowerUp3(by * 50, bx * 50)
            powerup_group3.add(new_power)
        if char == "5":
            f1x = by * 50
            f1y = bx * 50
        if char == "6":
            f2x = by * 50
            f2y = bx * 50
        if char == "7":
            f3x = by * 50
            f3y = bx * 50
        if char == "9":
            psx = by * 50
            psy = bx * 50
        if char == "8":
            f4x = by * 50
            f4y = bx * 50
        if by >= 22:
            by = 0
            bx = bx + 1
        else:
            by = by + 1

    file.close()

    # ---------------PLAYER DEFINITION------------

    class Pacman3(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            super().__init__()
            self.pacman_dx = psx
            self.pacman_dy = psy
            self.image = pygame.image.load("high.png")
            self.image = pygame.transform.scale(self.image, (35, 35))
            self.rect = self.image.get_rect()
            self.rect.topleft = [pos_x, pos_y]
            self.test = None
            self.lives = 3
            self.score = 0

        def update(self):
            self.rect.topleft = [self.pacman_dx, self.pacman_dy]

        def collisions(self):
            coll = pygame.sprite.spritecollide(pacman3, coins_group3, True, pygame.sprite.collide_rect)
            if coll:
                self.score += 1

        def get_position(self, n_x, n_y):
            self.pacman_dx += n_x
            self.pacman_dy += n_y

    pacman3 = Pacman3(0, 0)
    pacman_group3.add(pacman3)

    # ----------GHOSTS SET UP---------

    reset1x = f1x
    reset1y = f1y
    reset2x = f2x
    reset2y = f2y
    reset3x = f3x
    reset3y = f3y
    reset4x = f4x
    reset4y = f4y

    fanto1 = Phanto1_3(f1x, f1y)
    fanto2 = Phanto2_3(f2x, f2y)
    fanto3 = Phanto3_3(f3x, f3y)
    fanto4 = Phanto4_3(f4x, f4y)

    phanto1_group3.add(fanto1)
    phanto2_group3.add(fanto2)
    phanto3_group3.add(fanto3)
    phanto4_group3.add(fanto4)

    # ------------SPEED SET UP---------


    velocity = (0, 0)

    old_velocity = velocity


    p1velocity = (0, 0)
    p2velocity = (0, 0)
    p3velocity = (0, 0)
    p4velocity = (0, 0)

    oldv1 = p1velocity
    oldv2 = p2velocity
    oldv3 = p3velocity
    oldv4 = p4velocity

    # ----------------HUNTER TIMER----------


    ticker = 0

    # --------------LEVEL 1 GAME LOOP----------+

    while True:
        status = "PREY"
        checker = len(coins_group3.sprites())
        # victoria

        # ----------SPEEED UPDATER---------------
        ok = 1
        pacman3.get_position(velocity[0], velocity[1])
        oldv1 = p1velocity
        oldv2 = p2velocity
        oldv3 = p3velocity
        oldv4 = p4velocity
        f1x += p1velocity[0]
        f2x += p2velocity[0]
        f3x += p3velocity[0]
        f4x += p4velocity[0]
        f1y += p1velocity[1]
        f2y += p2velocity[1]
        f3y += p3velocity[1]
        f4y += p4velocity[1]
        fanto1.rect.topleft = [f1x, f1y]
        fanto2.rect.topleft = [f2x, f2y]
        fanto3.rect.topleft = [f3x, f3y]
        fanto4.rect.topleft = [f4x, f4y]

        pressedKeys = pygame.key.get_pressed()

        # ------------GETTING EVENTS-----------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pacman3.collisions()

        # ----------DECREASE/INCREASE SPEED--------

        if pressedKeys[pygame.K_c]:
            speed = 1

        if pressedKeys[pygame.K_v]:
            speed = 2

        if pressedKeys[pygame.K_b]:
            speed = 3

        if pressedKeys[pygame.K_ESCAPE]:
            pause = True
        if pressedKeys[pygame.K_SPACE]:
            pause = False

        # -------------GHOSTS DIRECTIONS------

        validator = 0
        validator = random.randint(1, 10)
        if validator == 1:
            hasher = 0
            uno = (0, -2 * speed)
            dos = (0, 2 * speed)
            tres = (2 * speed, 0)
            quatro = (-2 * speed, 0)
            hasher = random.randint(1, 4)
            if hasher == 1:
                p1velocity = uno
            if hasher == 2:
                p1velocity = dos
            if hasher == 3:
                p1velocity = tres
            if hasher == 4:
                p1velocity = quatro
            hasher = random.randint(1, 4)
            if hasher == 1:
                p2velocity = uno
            if hasher == 2:
                p2velocity = dos
            if hasher == 3:
                p2velocity = tres
            if hasher == 4:
                p2velocity = quatro
            hasher = random.randint(1, 4)
            if hasher == 1:
                p3velocity = uno
            if hasher == 2:
                p3velocity = dos
            if hasher == 3:
                p3velocity = tres
            if hasher == 4:
                p3velocity = quatro
            hasher = random.randint(1, 4)
            if hasher == 1:
                p4velocity = uno
            if hasher == 2:
                p4velocity = dos
            if hasher == 3:
                p4velocity = tres
            if hasher == 4:
                p4velocity = quatro

        # -----------GHOSTS COLLISIIONS-----------

        collf1 = pygame.sprite.spritecollide(fanto1, walls_group3, False, pygame.sprite.collide_rect)
        collf2 = pygame.sprite.spritecollide(fanto2, walls_group3, False, pygame.sprite.collide_rect)
        collf3 = pygame.sprite.spritecollide(fanto3, walls_group3, False, pygame.sprite.collide_rect)
        collf4 = pygame.sprite.spritecollide(fanto4, walls_group3, False, pygame.sprite.collide_rect)

        if collf1:
            f1x -= oldv1[0]
            f1y -= oldv1[1]

        if collf2:
            f2x -= oldv2[0]
            f2y -= oldv2[1]

        if collf3:
            f3x -= oldv3[0]
            f3y -= oldv3[1]

        if collf4:
            f4x -= oldv4[0]
            f4y -= oldv4[1]

        # -----------EATING SOBRANIE----------

        colli = pygame.sprite.spritecollide(pacman3, powerup_group3, True, pygame.sprite.collide_rect)
        if colli:
            pac_stronk.play()
            pacman3.score += 10
            new_power.respawn = True
            ticker = 300
            if new_power.respawn:
                ok = 1
                while ok == 1:
                    pow_x = random.randint(1, 12)
                    pow_y = random.randint(1, 20)
                    new_power = PowerUp3(pow_y * 50, pow_x * 50)
                    powerup_group3.add(new_power)
                    colio = pygame.sprite.spritecollide(new_power, walls_group3, False, pygame.sprite.collide_rect)
                    col1 = pygame.sprite.spritecollide(new_power, phanto1_group3, False, pygame.sprite.collide_rect)
                    col2 = pygame.sprite.spritecollide(new_power, phanto2_group3, False, pygame.sprite.collide_rect)
                    col3 = pygame.sprite.spritecollide(new_power, phanto3_group3, False, pygame.sprite.collide_rect)
                    col4 = pygame.sprite.spritecollide(new_power, phanto4_group3, False, pygame.sprite.collide_rect)
                    ok = 0
                    new_power.respawn = False
                    if colio or col1 or col2 or col3 or col4:
                        ok = 1
                        powerup_group3.remove(new_power)

        # ----------------HUNTING GHOSTS------------

        if ticker > 0:
            fanto1.weak = True
            fanto2.weak = True
            fanto3.weak = True
            fanto4.weak = True
            fanto1.image = pygame.image.load("scared.png")
            fanto1.image = pygame.transform.scale(fanto1.image, (50, 50))
            fanto2.image = pygame.image.load("scared.png")
            fanto2.image = pygame.transform.scale(fanto2.image, (50, 50))
            fanto3.image = pygame.image.load("scared.png")
            fanto3.image = pygame.transform.scale(fanto3.image, (50, 50))
            fanto4.image = pygame.image.load("scared.png")
            fanto4.image = pygame.transform.scale(fanto4.image, (50, 50))
            esc1 = False
            esc2 = False
            esc3 = False
            esc4 = False
            esc1 = pygame.sprite.spritecollide(pacman3, phanto1_group3, True, pygame.sprite.collide_rect)
            esc2 = pygame.sprite.spritecollide(pacman3, phanto2_group3, True, pygame.sprite.collide_rect)
            esc3 = pygame.sprite.spritecollide(pacman3, phanto3_group3, True, pygame.sprite.collide_rect)
            esc4 = pygame.sprite.spritecollide(pacman3, phanto4_group3, True, pygame.sprite.collide_rect)

            if esc1:
                pacman3.score += 25
                f1x = reset1x
                f1y = reset1y
                fanto1 = Phanto1_3(f1x, f1y)
                phanto1_group3.add(fanto1)
                ticker = 0
                pac_kill.play()

            if esc2:
                pacman3.score += 25
                f2x = reset2x
                f2y = reset2y
                fanto2 = Phanto2_3(f2x, f2y)
                phanto2_group3.add(fanto2)
                ticker = 0
                pac_kill.play()

            if esc3:
                pacman3.score += 25
                f3x = reset3x
                f3y = reset3y
                fanto3 = Phanto3_3(f3x, f3y)
                phanto3_group3.add(fanto3)
                ticker = 0
                pac_kill.play()

            if esc4:
                pacman3.score += 25
                f4x = reset4x
                f4y = reset4y
                fanto4 = Phanto4_3(f4x, f4y)
                phanto4_group3.add(fanto4)
                ticker = 0
                pac_kill.play()

            ticker -= 1
            status = "HUNTER"
        else:
            fanto1.weak = False
            fanto2.weak = False
            fanto3.weak = False
            fanto4.weak = False
            fanto1.image = pygame.image.load("fantored-Recovered.png")
            fanto1.image = pygame.transform.scale(fanto1.image, (50, 50))
            fanto2.image = pygame.image.load("fantopink.png")
            fanto2.image = pygame.transform.scale(fanto2.image, (50, 50))
            fanto3.image = pygame.image.load("fantoyell.png")
            fanto3.image = pygame.transform.scale(fanto3.image, (50, 50))
            fanto4.image = pygame.image.load("fantoturq.png")
            fanto4.image = pygame.transform.scale(fanto4.image, (50, 50))
            status = "PREY"

        # ------------------PACMAN COLLISIONS------------

        collw = pygame.sprite.spritecollide(pacman3, walls_group3, False, pygame.sprite.collide_rect)

        if collw:
            velocity = old_velocity
            pacman3.pacman_dy -= old_velocity[1]
            pacman3.pacman_dx -= old_velocity[0]
        pacman3.collisions()
        pacman_group3.update()

        collw1 = pygame.sprite.spritecollide(pacman3, phanto1_group3, False, pygame.sprite.collide_rect)
        collw2 = pygame.sprite.spritecollide(pacman3, phanto2_group3, False, pygame.sprite.collide_rect)
        collw3 = pygame.sprite.spritecollide(pacman3, phanto3_group3, False, pygame.sprite.collide_rect)
        collw4 = pygame.sprite.spritecollide(pacman3, phanto4_group3, False, pygame.sprite.collide_rect)

        if (collw1 and fanto1.weak == False) or (collw2 and fanto2.weak == False) or (
                collw3 and fanto3.weak == False) or (collw4 and fanto4.weak == False):
            pacman3.lives -= 1
            pac_dead.play()
            if pacman3.lives < 1:
                nivelas1.stop()
                gameover = pygame.image.load("gameoverwoo.png")
                gameover = pygame.transform.scale(gameover, (1400, 700))
                SCREEN.blit(gameover, (0, 0))
                pygame.display.update()
                clock.tick(60)
                time.sleep(3)
                SCREEN.fill("black")
                APHISH = Button(image=None, pos=(700, 250),
                                text_input="YOUR SCORE:", font=get_font(50), base_color="yellow",
                                hovering_color="magenta")
                APHISH.changeColor(LEVEL_1)
                APHISH.update(SCREEN)
                SCORE = Button(image=None, pos=(700, 350),
                               text_input=string, font=get_font(50), base_color="yellow", hovering_color="magenta")
                SCORE.changeColor(LEVEL_1)
                SCORE.update(SCREEN)
                pygame.display.update()
                time.sleep(2)
                main_menu()
            time.sleep(1)
            pacman3.pacman_dx = psx
            pacman3.pacman_dy = psy

        # ----------GETTING DIRECTIONS FORM PACMAN--------------

        if ok == 1:
            if pressedKeys[pygame.K_DOWN]:
                old_velocity = velocity
                velocity = (0, 1.5 * speed)
                ok = 0
        if ok == 1:
            if pressedKeys[pygame.K_UP]:
                old_velocity = velocity
                velocity = (0, -1.5 * speed)
                ok = 0
        if ok == 1:
            if pressedKeys[pygame.K_RIGHT]:
                old_velocity = velocity
                velocity = (1.5 * speed, 0)
                ok = 0
        if ok == 1:
            if pressedKeys[pygame.K_LEFT]:
                old_velocity = velocity
                velocity = (-1.5 * speed, 0)
                ok = 0

        if checker == 0:
            # += pacman3.score
            walls_group3.empty()
            powerup_group3.empty()
            phanto1_group3.empty()
            phanto2_group3.empty()
            phanto3_group3.empty()
            phanto4_group3.empty()
            pacman_group3.empty()
            level_1()

        # ---------GAME PAUSED/NOT PAUSED AND UPDATING THE SCREEN WITH THE PREVIOUS EVENTS----------

        if not pause:
            SCREEN.fill('black')
            string = str(pacman3.score)
            ss = str(pacman3.lives)
            APHISH = Button(image=None, pos=(1240, 100),
                            text_input="SCORE", font=get_font(20), base_color="yellow", hovering_color="magenta")
            APHISH.changeColor(LEVEL_1)
            APHISH.update(SCREEN)
            SCORE = Button(image=None, pos=(1240, 150),
                           text_input=string, font=get_font(20), base_color="yellow", hovering_color="magenta")
            SCORE.changeColor(LEVEL_1)
            SCORE.update(SCREEN)
            LIVES = Button(image=None, pos=(1250, 250),
                           text_input="REMAINED LIVES", font=get_font(20), base_color="yellow",
                           hovering_color="magenta")
            LIVES.changeColor(LEVEL_1)
            LIVES.update(SCREEN)
            NRL = Button(image=None, pos=(1245, 300),
                         text_input=ss, font=get_font(20), base_color="yellow", hovering_color="magenta")
            NRL.changeColor(LEVEL_1)
            NRL.update(SCREEN)
            STATUS = Button(image=None, pos=(1254, 450),
                            text_input="STATUS:", font=get_font(20), base_color="yellow",
                            hovering_color="magenta")
            STATUS.changeColor(LEVEL_1)
            STATUS.update(SCREEN)
            PH = Button(image=None, pos=(1245, 500),
                        text_input=status, font=get_font(20), base_color="yellow", hovering_color="magenta")
            PH.changeColor(LEVEL_1)
            PH.update(SCREEN)
            LEVEL_1 = pygame.mouse.get_pos()
            PLAY_BACK = Button(image=None, pos=(1245, 625),
                               text_input="BACK", font=get_font(75), base_color="White", hovering_color="magenta")

            PLAY_BACK.changeColor(LEVEL_1)
            PLAY_BACK.update(SCREEN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(LEVEL_1):
                        buttonel.set_volume(1.0)
                        buttonel.play(0)
                        play()
            coins_group3.draw(SCREEN)
            walls_group3.draw(SCREEN)
            powerup_group3.draw(SCREEN)
            phanto1_group3.draw(SCREEN)
            phanto2_group3.draw(SCREEN)
            phanto3_group3.draw(SCREEN)
            phanto4_group3.draw(SCREEN)
            pacman_group3.draw(SCREEN)
            phanto1_group3.update()
            phanto2_group3.update()
            phanto3_group3.update()
            phanto4_group3.update()
            pacman_group3.update()
            pygame.display.update()
            clock.tick(60)
        else:
            velocity = (0, 0)
            p1velocity = (0, 0)
            p2velocity = (0, 0)
            p3velocity = (0, 0)
            p4velocity = (0, 0)

def level_1():
    background.stop()
    nivelas2.play()
    pause = False
    speed = 1

    LEVEL_1 = pygame.mouse.get_pos()

    pacman_group2 = pygame.sprite.Group()

    coins_group2 = pygame.sprite.Group()

    walls_group2 = pygame.sprite.Group()

    powerup_group2 = pygame.sprite.Group()

    phanto1_group2 = pygame.sprite.Group()
    phanto2_group2 = pygame.sprite.Group()
    phanto3_group2 = pygame.sprite.Group()
    phanto4_group2 = pygame.sprite.Group()

    # ---------------MAP READING----------

    file = open('walls2.txt', 'r')
    bx = 0
    by = 0

    font = pygame.font.SysFont('Consolas', 30)

    f1x = 0
    f1y = 0
    f2x = 0
    f2y = 0
    f3x = 0
    f3y = 0
    f4x = 0
    f4y = 0

    while 1:

        char = file.read(1)
        if not char:
            break
        if char == "0":
            new_coin = Coins2(by * 25, bx * 25)
            coins_group2.add(new_coin)
        if char == "1":
            new_wall = Walls2(by * 25, bx * 25)
            walls_group2.add(new_wall)
        if char == "4":
            new_power = PowerUp2(by * 25, bx * 25)
            powerup_group2.add(new_power)
        if char == "5":
            f1x = by * 25
            f1y = bx * 25
        if char == "6":
            f2x = by * 25
            f2y = bx * 25
        if char == "7":
            f3x = by * 25
            f3y = bx * 25
        if char == "9":
            psx = by * 25
            psy = bx * 25
        if char == "8":
            f4x = by * 25
            f4y = bx * 25
        if by >= 44:
            by = 0
            bx = bx + 1
        else:
            by = by + 1

    file.close()

    # ---------------PLAYER DEFINITION------------

    class Pacman2(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            super().__init__()
            self.pacman_dx = psx
            self.pacman_dy = psy
            self.image = pygame.image.load("high.png")
            self.image = pygame.transform.scale(self.image, (20, 20))
            self.rect = self.image.get_rect()
            self.rect.topleft = [pos_x, pos_y]
            self.test = None
            self.lives = 3
            self.score = 0

        def update(self):
            self.rect.topleft = [self.pacman_dx, self.pacman_dy]

        def collisions(self):
            coll = pygame.sprite.spritecollide(pacman2, coins_group2, True, pygame.sprite.collide_rect)
            if coll:
                self.score += 1

        def get_position(self, n_x, n_y):
            self.pacman_dx += n_x
            self.pacman_dy += n_y

    pacman2 = Pacman2(0, 0)
    pacman_group2.add(pacman2)

    # ----------GHOSTS SET UP---------

    reset1x = f1x
    reset1y = f1y
    reset2x = f2x
    reset2y = f2y
    reset3x = f3x
    reset3y = f3y
    reset4x = f4x
    reset4y = f4y

    fanto1 = Phanto1_2(f1x, f1y)
    fanto2 = Phanto2_2(f2x, f2y)
    fanto3 = Phanto3_2(f3x, f3y)
    fanto4 = Phanto4_2(f4x, f4y)

    phanto1_group2.add(fanto1)
    phanto2_group2.add(fanto2)
    phanto3_group2.add(fanto3)
    phanto4_group2.add(fanto4)

    # ------------SPEED SET UP---------

    velocity = (0, 0)
    old_velocity = velocity

    p1velocity = (0, 0)
    p2velocity = (0, 0)
    p3velocity = (0, 0)
    p4velocity = (0, 0)

    oldv1 = p1velocity
    oldv2 = p2velocity
    oldv3 = p3velocity
    oldv4 = p4velocity

    # ----------------HUNTER TIMER----------
    ticker = 0

    # --------------LEVEL 1 GAME LOOP----------+

    while True:
        status = "PREY"
        checker = len(coins_group2.sprites())
        # victoria

        # ----------SPEEED UPDATER---------------
        ok = 1
        pacman2.get_position(velocity[0], velocity[1])
        oldv1 = p1velocity
        oldv2 = p2velocity
        oldv3 = p3velocity
        oldv4 = p4velocity
        f1x += p1velocity[0]
        f2x += p2velocity[0]
        f3x += p3velocity[0]
        f4x += p4velocity[0]
        f1y += p1velocity[1]
        f2y += p2velocity[1]
        f3y += p3velocity[1]
        f4y += p4velocity[1]
        fanto1.rect.topleft = [f1x, f1y]
        fanto2.rect.topleft = [f2x, f2y]
        fanto3.rect.topleft = [f3x, f3y]
        fanto4.rect.topleft = [f4x, f4y]

        pressedKeys = pygame.key.get_pressed()

        # ------------GETTING EVENTS-----------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pacman2.collisions()

        # ----------DECREASE/INCREASE SPEED--------

        if pressedKeys[pygame.K_c]:
            speed = 1

        if pressedKeys[pygame.K_v]:
            speed = 2

        if pressedKeys[pygame.K_b]:
            speed = 3

        if pressedKeys[pygame.K_ESCAPE]:
            pause = True
        if pressedKeys[pygame.K_SPACE]:
            pause = False

        # -------------GHOSTS DIRECTIONS------

        validator = 0
        validator = random.randint(1, 10)
        if validator == 1:
            hasher = 0
            uno = (0, -2 * speed)
            dos = (0, 2 * speed)
            tres = (2 * speed, 0)
            quatro = (-2 * speed, 0)
            hasher = random.randint(1, 4)
            if hasher == 1:
                p1velocity = uno
            if hasher == 2:
                p1velocity = dos
            if hasher == 3:
                p1velocity = tres
            if hasher == 4:
                p1velocity = quatro
            hasher = random.randint(1, 4)
            if hasher == 1:
                p2velocity = uno
            if hasher == 2:
                p2velocity = dos
            if hasher == 3:
                p2velocity = tres
            if hasher == 4:
                p2velocity = quatro
            hasher = random.randint(1, 4)
            if hasher == 1:
                p3velocity = uno
            if hasher == 2:
                p3velocity = dos
            if hasher == 3:
                p3velocity = tres
            if hasher == 4:
                p3velocity = quatro
            hasher = random.randint(1, 4)
            if hasher == 1:
                p4velocity = uno
            if hasher == 2:
                p4velocity = dos
            if hasher == 3:
                p4velocity = tres
            if hasher == 4:
                p4velocity = quatro

        # -----------GHOSTS COLLISIIONS-----------

        collf1 = pygame.sprite.spritecollide(fanto1, walls_group2, False, pygame.sprite.collide_rect)
        collf2 = pygame.sprite.spritecollide(fanto2, walls_group2, False, pygame.sprite.collide_rect)
        collf3 = pygame.sprite.spritecollide(fanto3, walls_group2, False, pygame.sprite.collide_rect)
        collf4 = pygame.sprite.spritecollide(fanto4, walls_group2, False, pygame.sprite.collide_rect)

        if collf1:
            f1x -= oldv1[0]
            f1y -= oldv1[1]

        if collf2:
            f2x -= oldv2[0]
            f2y -= oldv2[1]

        if collf3:
            f3x -= oldv3[0]
            f3y -= oldv3[1]

        if collf4:
            f4x -= oldv4[0]
            f4y -= oldv4[1]

        # -----------EATING SOBRANIE----------

        colli = pygame.sprite.spritecollide(pacman2, powerup_group2, True, pygame.sprite.collide_rect)
        if colli:
            pac_stronk.play()
            pacman2.score += 10
            new_power.respawn = True
            ticker = 300
            if new_power.respawn:
                ok = 1
                while ok == 1:
                    pow_x = random.randint(1, 26)
                    pow_y = random.randint(1, 42)
                    new_power = PowerUp2(pow_y * 25, pow_x * 25)
                    powerup_group2.add(new_power)
                    colio = pygame.sprite.spritecollide(new_power, walls_group2, False, pygame.sprite.collide_rect)
                    col1 = pygame.sprite.spritecollide(new_power, phanto1_group2, False, pygame.sprite.collide_rect)
                    col2 = pygame.sprite.spritecollide(new_power, phanto2_group2, False, pygame.sprite.collide_rect)
                    col3 = pygame.sprite.spritecollide(new_power, phanto3_group2, False, pygame.sprite.collide_rect)
                    col4 = pygame.sprite.spritecollide(new_power, phanto4_group2, False, pygame.sprite.collide_rect)
                    ok = 0
                    new_power.respawn = False
                    if colio or col1 or col2 or col3 or col4:
                        ok = 1
                        powerup_group2.remove(new_power)

        # ----------------HUNTING GHOSTS------------

        if ticker > 0:
            fanto1.weak = True
            fanto2.weak = True
            fanto3.weak = True
            fanto4.weak = True
            fanto1.image = pygame.image.load("scared.png")
            fanto1.image = pygame.transform.scale(fanto1.image, (25, 25))
            fanto2.image = pygame.image.load("scared.png")
            fanto2.image = pygame.transform.scale(fanto2.image, (25, 25))
            fanto3.image = pygame.image.load("scared.png")
            fanto3.image = pygame.transform.scale(fanto3.image, (25, 25))
            fanto4.image = pygame.image.load("scared.png")
            fanto4.image = pygame.transform.scale(fanto4.image, (25, 25))
            esc1 = False
            esc2 = False
            esc3 = False
            esc4 = False
            esc1 = pygame.sprite.spritecollide(pacman2, phanto1_group2, True, pygame.sprite.collide_rect)
            esc2 = pygame.sprite.spritecollide(pacman2, phanto2_group2, True, pygame.sprite.collide_rect)
            esc3 = pygame.sprite.spritecollide(pacman2, phanto3_group2, True, pygame.sprite.collide_rect)
            esc4 = pygame.sprite.spritecollide(pacman2, phanto4_group2, True, pygame.sprite.collide_rect)

            if esc1:
                pacman2.score += 25
                f1x = reset1x
                f1y = reset1y
                fanto1 = Phanto1_2(f1x, f1y)
                phanto1_group2.add(fanto1)
                ticker = 0
                pac_kill.play()

            if esc2:
                pacman2.score += 25
                f2x = reset2x
                f2y = reset2y
                fanto2 = Phanto2_2(f2x, f2y)
                phanto2_group2.add(fanto2)
                ticker = 0
                pac_kill.play()

            if esc3:
                pacman2.score += 25
                f3x = reset3x
                f3y = reset3y
                fanto3 = Phanto3_2(f3x, f3y)
                phanto3_group2.add(fanto3)
                ticker = 0
                pac_kill.play()

            if esc4:
                pacman2.score += 25
                f4x = reset4x
                f4y = reset4y
                fanto4 = Phanto4_2(f4x, f4y)
                phanto4_group2.add(fanto4)
                ticker = 0
                pac_kill.play()

            ticker -= 1
            status = "HUNTER"
        else:
            fanto1.weak = False
            fanto2.weak = False
            fanto3.weak = False
            fanto4.weak = False
            fanto1.image = pygame.image.load("fantored-Recovered.png")
            fanto1.image = pygame.transform.scale(fanto1.image, (25, 25))
            fanto2.image = pygame.image.load("fantopink.png")
            fanto2.image = pygame.transform.scale(fanto2.image, (25, 25))
            fanto3.image = pygame.image.load("fantoyell.png")
            fanto3.image = pygame.transform.scale(fanto3.image, (25, 25))
            fanto4.image = pygame.image.load("fantoturq.png")
            fanto4.image = pygame.transform.scale(fanto4.image, (25, 25))
            status = "PREY"

        # ------------------PACMAN COLLISIONS------------

        collw = pygame.sprite.spritecollide(pacman2, walls_group2, False, pygame.sprite.collide_rect)

        if collw:
            velocity = old_velocity
            pacman2.pacman_dy -= old_velocity[1]
            pacman2.pacman_dx -= old_velocity[0]
        pacman2.collisions()
        pacman_group2.update()

        collw1 = pygame.sprite.spritecollide(pacman2, phanto1_group2, False, pygame.sprite.collide_rect)
        collw2 = pygame.sprite.spritecollide(pacman2, phanto2_group2, False, pygame.sprite.collide_rect)
        collw3 = pygame.sprite.spritecollide(pacman2, phanto3_group2, False, pygame.sprite.collide_rect)
        collw4 = pygame.sprite.spritecollide(pacman2, phanto4_group2, False, pygame.sprite.collide_rect)

        if (collw1 and fanto1.weak == False) or (collw2 and fanto2.weak == False) or (
                collw3 and fanto3.weak == False) or (collw4 and fanto4.weak == False):
            pacman2.lives -= 1
            pac_dead.play()
            if pacman2.lives < 1:
                nivelas3.stop()
                gameover = pygame.image.load("gameoverwoo.png")
                gameover = pygame.transform.scale(gameover, (1400, 700))
                SCREEN.blit(gameover, (0, 0))
                pygame.display.update()
                clock.tick(60)
                time.sleep(3)
                SCREEN.fill("black")
                APHISH = Button(image=None, pos=(700, 250),
                                text_input="YOUR SCORE:", font=get_font(50), base_color="yellow",
                                hovering_color="magenta")
                APHISH.changeColor(LEVEL_1)
                APHISH.update(SCREEN)
                SCORE = Button(image=None, pos=(700, 350),
                               text_input=string, font=get_font(50), base_color="yellow", hovering_color="magenta")
                SCORE.changeColor(LEVEL_1)
                SCORE.update(SCREEN)
                pygame.display.update()
                time.sleep(2)
                main_menu()
            time.sleep(1)
            pacman2.pacman_dx = psx
            pacman2.pacman_dy = psy

        # ----------GETTING DIRECTIONS FORM PACMAN--------------

        if ok == 1:
            if pressedKeys[pygame.K_DOWN]:
                old_velocity = velocity
                velocity = (0, 1.5 * speed)
                ok = 0
        if ok == 1:
            if pressedKeys[pygame.K_UP]:
                old_velocity = velocity
                velocity = (0, -1.5 * speed)
                ok = 0
        if ok == 1:
            if pressedKeys[pygame.K_RIGHT]:
                old_velocity = velocity
                velocity = (1.5 * speed, 0)
                ok = 0
        if ok == 1:
            if pressedKeys[pygame.K_LEFT]:
                old_velocity = velocity
                velocity = (-1.5 * speed, 0)
                ok = 0

        if checker == 0:
            #global_score += pacman2.score
            walls_group2.empty()
            powerup_group2.empty()
            phanto1_group2.empty()
            phanto2_group2.empty()
            phanto3_group2.empty()
            phanto4_group2.empty()
            pacman_group2.empty()
            level_3()

        # ---------GAME PAUSED/NOT PAUSED AND UPDATING THE SCREEN WITH THE PREVIOUS EVENTS----------

        if not pause:
            SCREEN.fill('black')
            string = str(pacman2.score)
            ss = str(pacman2.lives)
            APHISH = Button(image=None, pos=(1240, 100),
                            text_input="SCORE", font=get_font(20), base_color="yellow", hovering_color="magenta")
            APHISH.changeColor(LEVEL_1)
            APHISH.update(SCREEN)
            SCORE = Button(image=None, pos=(1240, 150),
                           text_input=string, font=get_font(20), base_color="yellow", hovering_color="magenta")
            SCORE.changeColor(LEVEL_1)
            SCORE.update(SCREEN)
            LIVES = Button(image=None, pos=(1250, 250),
                           text_input="REMAINED LIVES", font=get_font(20), base_color="yellow",
                           hovering_color="magenta")
            LIVES.changeColor(LEVEL_1)
            LIVES.update(SCREEN)
            NRL = Button(image=None, pos=(1245, 300),
                         text_input=ss, font=get_font(20), base_color="yellow", hovering_color="magenta")
            NRL.changeColor(LEVEL_1)
            NRL.update(SCREEN)
            STATUS = Button(image=None, pos=(1254, 450),
                            text_input="STATUS:", font=get_font(20), base_color="yellow",
                            hovering_color="magenta")
            STATUS.changeColor(LEVEL_1)
            STATUS.update(SCREEN)
            PH = Button(image=None, pos=(1245, 500),
                        text_input=status, font=get_font(20), base_color="yellow", hovering_color="magenta")
            PH.changeColor(LEVEL_1)
            PH.update(SCREEN)
            LEVEL_1 = pygame.mouse.get_pos()
            PLAY_BACK = Button(image=None, pos=(1245, 625),
                               text_input="BACK", font=get_font(75), base_color="White", hovering_color="magenta")

            PLAY_BACK.changeColor(LEVEL_1)
            PLAY_BACK.update(SCREEN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(LEVEL_1):
                        buttonel.set_volume(1.0)
                        buttonel.play(0)
                        play()
            coins_group2.draw(SCREEN)
            walls_group2.draw(SCREEN)
            powerup_group2.draw(SCREEN)
            phanto1_group2.draw(SCREEN)
            phanto2_group2.draw(SCREEN)
            phanto3_group2.draw(SCREEN)
            phanto4_group2.draw(SCREEN)
            pacman_group2.draw(SCREEN)
            phanto1_group2.update()
            phanto2_group2.update()
            phanto3_group2.update()
            phanto4_group2.update()
            pacman_group2.update()
            pygame.display.update()
            clock.tick(60)
        else:
            velocity = (0, 0)
            p1velocity = (0, 0)
            p2velocity = (0, 0)
            p3velocity = (0, 0)
            p4velocity = (0, 0)


main_menu()

pygame.quit()
sys.exit()
