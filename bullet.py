# coding="utf-8"
# author : "Jayson"
# bullet module

# zh-cn:导入pygame模块
# en:import the pygame module
import pygame

bullet_move_speed = 4

class Bullet(object):

    def __init__(self,win,hero_x,hero_y,hero_width):
        # 加载图片;loading image
        self.img = pygame.image.load("res/hero_bullet_7.png")

        # 获取窗口对象;get window object
        self.window = win

        # 设置矩形对象;set the rectangle object
        self.bullet_rect = self.img.get_rect()

        # 设置矩形的位置; set the rectangle's position
        self.bullet_rect[1] = hero_y - self.bullet_rect[3]
        self.bullet_rect[0] = hero_x + hero_width/2 - self.bullet_rect[2]/2

    def move(self):
        # 设置子弹速度;set bullet speed
        self.bullet_rect[1] -= bullet_move_speed

    # 绘制背景；draw into window
    def blited(self):
        self.window.blit(self.img,(self.bullet_rect[0],self.bullet_rect[1]))
