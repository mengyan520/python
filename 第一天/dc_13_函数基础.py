def sum(a, b):
    return a + b


def run():
    """跑"""
    print("跑")


def print_lines(char, time, count):
    """
分割线
    :param char: 字符                                                                                                   
    :param time: 总数
    :param count: 次数
    """
    while count > 0:
        count -= 1
        print(char * time)


print(sum(1, 2))

run()

print_lines("*",50,5)

