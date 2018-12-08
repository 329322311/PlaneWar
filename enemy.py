# coding="utf-8"
# author : "Jayson"
# enemy module

# zh-cn:导入pygame模块
# en:import the pygame module
import pygame
import random,setting



class Enemy(object):

    def __init__(self,win):
        # 加载图片;loading image
        self.img = pygame.image.load("res/img-plane_%s.png" % random.randint(1,7))

        # 获取窗口对象;get window object
        self.window = win

        # 设置敌机的矩形对象;set the enemys' rectangle object
        self.enemy_rect = self.img.get_rect()

        # 设置矩形的位置; set the rectangle's position
        self.enemy_rect[1] = random.randint(-300,0)
        self.enemy_rect[0] = random.randint(0,setting.WIN_WIDTH-self.enemy_rect[2])

        self.speed = random.randint(30, 40) * 0.1

    def move(self):
        self.enemy_rect[1] += self.speed

        # 当飞机超过窗口时，飞机重置;the enemy resets when it passed the window
        if self.enemy_rect[1] > setting.WIN_HEIGHT:
            self.enemy_reset()

    # 重置方法;reset method
    def enemy_reset(self):
        self.img = pygame.image.load("res/img-plane_%s.png" % random.randint(1, 7))
        self.enemy_rect[1] = random.randint(-300, 0)
        self.enemy_rect[0] = random.randint(0, setting.WIN_WIDTH - self.enemy_rect[2])
        self.speed = random.randint(30,45) * 0.1

    # 绘制背景；draw background into window
    def blited(self):
        self.window.blit(self.img,(self.enemy_rect[0],self.enemy_rect[1]))
