from collections import Iterable
from collections import Iterator


class Person(object):
    def __init__(self):
        self.names = list()
        self.index = 0

    # 让类成为迭代器
    def __iter__(self):
        return self

    # 返回迭代的内容
    def __next__(self):
        if self.index < len(self.names):
            name = self.names[self.index]
            self.index += 1
            return name
        # 抛出异常，停止迭代
        else:
            raise StopIteration


person = Person()
# 是否可迭代
print(isinstance(person, Iterable))
# 是否是迭代器
print(isinstance(person, Iterator))
person.names.append("张三")
person.names.append("李四")
for name in person:
    print(name)
