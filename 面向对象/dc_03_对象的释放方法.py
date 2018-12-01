class Person:
    def __init__(self,name):
        self.name = name

    def getName(self):
        print("我的名字：%s" % self.name)

    def __del__(self):
        print ("这个对象被释放了")

person =Person("单车")
person.getName()
# del person
print ("-" * 50)