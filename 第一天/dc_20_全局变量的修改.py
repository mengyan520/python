num = 10


def demo1():
    # global声明，方可修改全局变量的值，会告诉解释器，这个变量是全局的
    global num
    num = 100
    print(num)


demo1()
