import pygame

pygame.init()
# 创建窗口
screen = pygame.display.set_mode((480,700))
# 加载背景图片
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0,0))
# 绘制英雄图片
hero1 = pygame.image.load("./images/hero1.png")
screen.blit(hero1, (200,500))
pygame.display.update()
# 创建游戏时钟
clock = pygame.time.Clock()
while True:
    clock.tick(1)
    print(pygame.event.get())

pygame.quit()