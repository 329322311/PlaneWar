# coding="utf-8" #<br>
# author : "Jayson"<br>
# zh-cn:导入pygame模块
# en:import the pygame module
import pygame

# 初始化pygame
# Initialization of pygame
pygame.init()

# 创建飞机大战的大类
# Create class of PlaneWar
class PlaneWar(object):

    def __init__(self): # 定义初始值；define the initial value
        pass

    def events(self):   # 定义事件方法；define events method；
        pass

    def move(self):     # 定义移动方法；define a movement method
        pass

    def blit(self):     # 定义子弹方法；define bullet method
        pass

    def display(self):  # 定义显示方法；define display method
        pass

    def run(self):      # 定义运行方法；define the operation method
        while True:

            # 1、调用事件方法；run events method
            self.events()
            # 2、各个对象的移动；run a movement method
            self.move()
            # 3、绘制图片对象；run a bullet method
            self.blit()
            # 4、更新界面；update display content
            self.display()

if __name__ =="__main__":
    game = PlaneWar()   # 创建game对象；Create game object
    game.run()  # 运行；run the game
