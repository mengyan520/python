import random
player = int(input("请输入您要出的拳 石头（1）剪刀（2）布（3）\n"))
computer = random.randint(1,3)
if player == 1:
    print("玩家选择的是石头")
elif player == 2:
    print("玩家选择的是剪刀")
else:
    print("玩家选择的是布")

if computer == 1:
    print("电脑选择的是石头")
elif computer == 2:
    print("电脑选择的是剪刀")
else:
    print("电脑选择的是布")
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("玩家赢")
elif player == computer:
    print("平局")
else:
    print("电脑赢")