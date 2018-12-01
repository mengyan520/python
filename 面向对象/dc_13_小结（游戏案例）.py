class Game(object):
    # 历史最高分
    top_score = 0
    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("显示帮组")
    @classmethod
    def show_top_score(cls):
        print("历史最好分：",cls.top_score)

    def start_game(self):
        print("%s 开始玩游戏" % self.player_name)


Game.show_help()
Game.show_top_score()
player = Game("小明")
player.start_game()
