class Person:
    def __init__(self, weight, name):
        self.weight = weight
        self.name = name

    def run(self):
        self.weight -= 0.5
        print ("%s 跑步，减肥0.5公斤,现在体重 %.1f" % (self.name, self.weight))

    def eat(self):
        self.weight += 1
        print ("%s 吃饭，增加1公斤,现在体重 %.1f" % (self.name, self.weight))

    def __str__(self):
        return "我叫%s，体重%.1f" % (self.name, self.weight)


person = Person(130, "小明")
person.eat()
person.run()
print(person)
