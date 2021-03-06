# coding="utf-8"
# author : "Jayson"
# structure first
# zh-cn:导入pygame,sys模块
# en:import the pygame,sys module

import pygame,sys,setting

# 创建飞机大战的大类
# Create class of PlaneWar
from enemy import Enemy
from hero import Hero
from map import Map


class PlaneWar(object):


    def __init__(self): # 定义初始值;define the initial value
        # 初始化pygame
        # Initialization of pygame
        pygame.init()

        # 创建窗口;set window sizes
        window = pygame.display.set_mode([setting.WIN_WIDTH, setting.WIN_HEIGHT])

        # 调用设置窗口;run setting window properties
        self.set_window()

        # 创建对象;create objects
        self.map = Map(window)
        self.hero = Hero(window)
        self.enemy = [Enemy(window) for _ in range(4)]

    @staticmethod
    def set_window():
        # 设置窗口标题;set window caption
        pygame.display.set_caption("AirWar1.0")
        # 加载窗口图标;load window's image
        icon = pygame.image.load("res/game.ico")
        # 设置窗口图标;set window's image
        pygame.display.set_icon(icon)

    # 定义事件方法;define events method
    def events(self):
        # 获取响应事件;get the events in response
        event_list = pygame.event.get()
        # 遍历事件;traversal events
        for event in event_list:
            # 鼠标点击关闭窗口事件（解决未响应）;exit event
            if event.type == pygame.QUIT:
                print("关闭了窗口")
                sys.exit()
            # 判断是否空格;if press space,shoot
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.hero.shooting()

    # 定义移动方法；define a movement method
    def move(self):
        self.map.move()
        self.hero.move()

        # 每一个子弹都需要调用自己的move方法;each bullet needs to call its own move method
        for i in self.hero.bullets:
            i.move()

        # 移动每一个敌机;move each enemy
        for i in self.enemy:
            i.move()

    def hit_enemy(self):
        # 判断两个矩形是否相交，相交返回True，否则返回False;to determine whether two rectangles intersect, the intersection returns True or False
        for i in self.hero.bullets:
            for j in self.enemy:
                if pygame.Rect.colliderect(i.bullet_rect, j.enemy_rect):
                    j.enemy_reset()

    def crash(self):
        # 判断两个矩形是否相交，相交返回True，否则返回False;to determine whether two rectangles intersect, the intersection returns True or False
        for i in self.enemy:
                if pygame.Rect.colliderect(i.enemy_rect, self.hero.hero_rect):
                    return True
        else:
            return False

    # 定义绘制方法；define the drawing method
    def blit(self):
        self.map.blited()
        self.hero.blited()

        # 遍历绘制敌机;iterating over to draw the enemys
        for i in self.enemy:
            i.blited()

    # 定义显示方法；define display method
    def display(self):
        pygame.display.update()

    def gameover(self):
        while True:
            # 获取响应事件;get the events in response
            event_list = pygame.event.get()
            # 遍历事件;traversal events
            for event in event_list:
                # 鼠标点击关闭窗口事件（解决未响应）;exit event
                if event.type == pygame.QUIT:
                    print("关闭了窗口")
                    sys.exit()

    # 定义运行方法；define the operation method
    def run(self):
        while True:

            # 1.调用事件方法；run events method
            self.events()
            # 2.各个对象的移动；run a movement method
            self.move()
            # 3.判断是否打中敌机;judge whether you hit the enemys
            self.hit_enemy()
            if self.crash():
                break
            # 4.绘制图片对象；run a bullet method
            self.blit()
            # 5.更新界面；update display content
            self.display()
        self.gameover()

if __name__ =="__main__":
    # 创建game对象；Create game object
    game = PlaneWar()
    # 运行；run the game
    game.run()
