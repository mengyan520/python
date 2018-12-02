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
while True:
    # 注意：只有在有游戏循环里面进行一些事件操作，程序才能正常运行
    print(pygame.event.get())
pygame.quit()