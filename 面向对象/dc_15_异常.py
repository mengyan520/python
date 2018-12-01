try:
    num = int(input("请输入整数："))
except:
    print("请输入整数")

try:
    result = 8 / num
except ZeroDivisionError:
    print("不能输入0")
except Exception as re:
    print(re)
except:
    print("无法识别")
else:
    print("输入成功,没有异常")
finally:
    print("无论如何都和执行")
