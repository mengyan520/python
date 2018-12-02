import pygame
from plane_sprite import *
pygame.init()
# 创建窗口
screen = pygame.display.set_mode((480,700))
# 加载背景图片
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0,0))
# 绘制英雄图片
hero1 = pygame.image.load("./images/hero1.png")
screen.blit(hero1, (150,300))
pygame.display.update()
# 创建游戏时钟
clock = pygame.time.Clock()
# 更新英雄位置
hero_rect = pygame.Rect(150,300,100,124)

# 创建敌机精灵
enemy = GameSprite("./images/enemy0.png")
enemy1 = GameSprite("./images/enemy1.png",2)
# 创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)


while True:
    clock.tick(60)
    hero_rect.y -= 5
    # 判断飞机位置
    if hero_rect.y <=0:
        hero_rect.y = 700
    # 绘制背景图片，覆盖原来图层
    screen.blit(bg, (0,0))
    # 绘制英雄图像
    screen.blit(hero1, hero_rect)
    # 让精灵组调用方法
    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.update()
    for event in pygame.event.get():
        #  判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏")
            pygame.quit()
            exit()
