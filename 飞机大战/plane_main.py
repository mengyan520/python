import pygame
from plane_sprite import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        # 创建窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，精灵和精灵组的创建
        self.__creat_sprites()
        # 设置敌机出现定时器
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 500)
        # 英雄发射子弹
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def start_game(self):
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

    def __creat_sprites(self):
        # 创建背景图片
        bg1 = Background()
        bg2 = Background(True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    # 事件监听
    def __event_handler(self):
        for event in pygame.event.get():
            #  判断用户是否点击了关闭按钮
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_RIGHT]:
                self.hero.speed = 20
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -20
            else:
                self.hero.speed = 0

    # 碰撞检测
    def __check_collide(self):
        # 子弹和敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 英雄和敌机
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies):
            self.hero.kill()
            PlaneGame.__game_over()

    # 更新/绘制精灵组
    def __update_sprites(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    # 结束游戏
    @staticmethod
    def __game_over():
        print("退出游戏")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
