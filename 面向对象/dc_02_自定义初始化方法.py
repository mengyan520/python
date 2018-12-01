class Person:
    def __init__(self,name):
        self.name = name
    def getName(self):
        print("我的名字：%s" % self.name)

person = Person("单车")
person.getName()
