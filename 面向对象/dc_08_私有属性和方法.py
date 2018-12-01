class Person:
    def __init__(self, name,):
        self.name = name
        self.__age = 20

    def __getAge(self):
        print("我的年龄是 %d" % self.__age)
    def __str__(self):
        self.__getAge()
        return "这是私有的"


person1 = Person("单车")
print(person1)
# 访问私有属性
person1._Person__getAge()
print(person1._Person__age)