# coding="utf-8"
# author : "Jayson"
# hero module

# zh-cn:导入pygame模块
# en:import the pygame module
import pygame
import setting
from bullet import Bullet


class Hero(object):

    def __init__(self,win):
        # 加载英雄飞机;loading the hero plane
        self.img = pygame.image.load("res/hero2.png")

        # 获取窗口对象;get window object
        self.window = win

        # 设置英雄的矩形对象;set the hero's rectangle object
        self.hero_rect = self.img.get_rect()

        # 设置矩形的位置; set the rectangle's position
        self.hero_rect[1] = 600
        self.hero_rect[0] = setting.WIN_WIDTH / 2 - self.hero_rect[2] / 2

        # 携带的子弹;cartridge
        self.bullets = []

    def move(self):
        # 获得当前键盘所有按键的状态(按下，没有按下)，返回bool元组;get the status of all keys on the current keyboard (pressed, not pressed) and returns the bool tuple
        pressed_keys = pygame.key.get_pressed()

        # 设上边界;set top boundary
        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            if self.hero_rect[1] > -self.hero_rect[3] / 2:
                self.hero_rect[1] -= setting.plane_move_speed

        # 设下边界;set bottom boundary
        if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
            if self.hero_rect[1] < setting.WIN_HEIGHT - self.hero_rect[3] / 2:
                self.hero_rect[1] += setting.plane_move_speed

        # 设左边界;set left boundary
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            if self.hero_rect[0] > -self.hero_rect[2] / 2:
                self.hero_rect[0] -= setting.plane_move_speed

        # 设右边界;set right boundary
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            if self.hero_rect[0] < setting.WIN_WIDTH - self.hero_rect[2] / 2:
                self.hero_rect[0] += setting.plane_move_speed

    # 射击功能;shooting method
    def shooting(self):
        self.bullets.append(Bullet(self.window,self.hero_rect[0],self.hero_rect[1],self.hero_rect[2]))

    # 绘制背景；draw background into window
    def blited(self):
        self.window.blit(self.img,(self.hero_rect[0],self.hero_rect[1]))

        # 子弹的绘制;draw bullets
        # 子弹超出边界就删除掉对象;the bullets cross the boundary and deletes the object
        for i in self.bullets:
            if i.bullet_rect[1] < -i.bullet_rect[3]/2:
                self.bullets.remove(i)
            else:
                i.blited()
