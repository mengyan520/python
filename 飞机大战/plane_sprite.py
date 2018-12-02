import random
import pygame

# 屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PER_SEC = 60
# 敌机出现事件
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect: pygame.Rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 垂直移动
        self.rect.y += self.speed


class Background(GameSprite):
    """背景精灵"""

    def __init__(self, is_alt=False):
        super().__init__("./images/background.png", 10)
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        # 判断是否移出屏幕,如果移出，将图像设置到屏幕的正上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        super().__init__("./images/enemy0.png")
        self.speed = random.randint(10, 20)
        self.rect.x = random.randint(0, (SCREEN_RECT.width - self.rect.width))

    def update(self):
        super().update()
        # 大于屏幕，移除
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        # print("敌机挂了")
        pass


class Hero(GameSprite):
    """英雄飞机"""

    def __init__(self):
        super().__init__("./images/hero1.png", 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        for i in (0, 1, 2):
            bullet: Bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹类"""

    def __init__(self):
        super().__init__("./images/bullet.png", -5)

    def update(self):
        super().update()
        # 大于屏幕，移除
        if self.rect.bottom <= 0:
            self.kill()
