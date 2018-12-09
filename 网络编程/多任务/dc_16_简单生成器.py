def creat_num(all_num):
    """生成器模版"""
    a, b = 0, 1
    index = 0
    while index < all_num:
        # 一开始代码会停到这，之后每次循环从这开始
        yield a
        a, b = b, a + b
        index += 1
    return "ok"


obj = creat_num(10)
while True:
    try:
        ret = next(obj)
        print(ret)
    except Exception as res:
        print(res)
        break


