def demo1(num):
    if num == 1:
        return 1
    temp = demo1(num - 1)
    return num + temp


print(demo1(100))