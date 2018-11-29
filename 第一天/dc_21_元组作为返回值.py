def demo1():
    num = 10
    age = 20
    # 省略小括号
    return num, age


print(demo1())


def demo2():
    return "栈单", "单车"


name1, name2 = demo2()
print(name1)
print(name2)
# 交换两个变量
a = 10
b = 20
# 右边其实是元组，括号省略了
a, b = b, a
print(a)
print(b)