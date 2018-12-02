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
# 更新英雄位置
hero_rect = pygame.Rect(200,500,100,124)
while True:
    clock.tick(60)
    hero_rect.y -= 1
    # 绘制背景图片，覆盖原来图层
    screen.blit(bg, (0,0))
    # 绘制英雄图像
    screen.blit(hero1, hero_rect)
    pygame.display.update()
    print(pygame.event.get())

pygame.quit()