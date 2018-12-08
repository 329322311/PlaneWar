# coding="utf-8"
# author : "Jayson"
# map module

# zh-cn:导入pygame模块
# en:import the pygame module
import pygame

WIN_WIDTH = 512
WIN_HEIGHT = 768
map_move_speed = 2

class Map(object):

    def __init__(self,win):
        # 加载两张背景图片;load two background images
        self.img = pygame.image.load("res/img_bg_level_1.jpg")
        self.img2 = pygame.image.load("res/img_bg_level_1.jpg")

        # 获取窗口对象;get window object
        self.window = win

        # 设置两张图片的y值;set the y values for both images
        self.y = 0
        self.y2 = -WIN_HEIGHT

    def move(self):
        # 地图的移动；set map movement
        self.y += map_move_speed
        self.y2 += map_move_speed
        if self.y > WIN_HEIGHT:
            self.y = -WIN_HEIGHT
        if self.y2 > WIN_HEIGHT:
            self.y2 = -WIN_HEIGHT

    # 绘制背景;draw background into window
    def blited(self):
        self.window.blit(self.img,(0,self.y))
        self.window.blit(self.img2,(0, self.y2))

