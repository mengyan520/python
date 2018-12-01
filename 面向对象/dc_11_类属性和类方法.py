class Person(object):
    age = 18
    def __init__(self, name):
        self.name = name
    # 类方法
    @classmethod
    def getAge(cls):
        print("父类年龄：",cls.age)


person = Person("单车")
print(person.age)
# 如果定义了同名的属性,会先调用对象的属性
person.age = 20
print(person.age)
print(Person.age)
Person.getAge()
