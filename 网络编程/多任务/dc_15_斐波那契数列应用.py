class Fibonacci(object):
    def __init__(self,all_num):
        self.all_num = all_num
        self.a = 0
        self.b = 1
        self.index = 0

    # 让类成为迭代器
    def __iter__(self):
        return self

    # 返回迭代的内容
    def __next__(self):
        if self.index < self.all_num:
            ret = self.a
            # 从右原则，右边表达式先赋值
            self.a, self.b = self.b, self.a+self.b
            self.index += 1
            return ret
        # 抛出异常，停止迭代
        else:
            raise StopIteration


fib= Fibonacci(10)
for num in fib:
    print(num)
