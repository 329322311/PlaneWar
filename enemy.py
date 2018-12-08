# coding="utf-8"
# author : "Jayson"
# enemy module

# zh-cn:导入pygame模块
# en:import the pygame module
import pygame
import random

WIN_WIDTH = 512

class Enemy(object):

    def __init__(self,win):
        # 加载图片;loading image
        self.img = pygame.image.load("res/img-plane_%s.png" % random.randint(1,7))

        # 获取窗口对象;get window object
        self.window = win

        # 设置敌机的矩形对象;set the enemys' rectangle object
        self.enemy_rect = self.img.get_rect()

        # 设置矩形的位置; set the rectangle's position
        self.enemy_rect[1] = 0
        self.enemy_rect[0] = random.randint(0,WIN_WIDTH-self.enemy_rect[2])

    def move(self):
        pass

    # 绘制背景；draw background into window
    def blited(self):
        self.window.blit(self.img,(self.enemy_rect[0],self.enemy_rect[1]))
