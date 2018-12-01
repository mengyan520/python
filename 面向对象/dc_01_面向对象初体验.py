class Cat:
    # 初始化方法
    def __init__(self):
        # 属性
        self.name = "猫"
    # 对象方法
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


# 创建对象
cat = Cat()
cat.eat()
cat.drink()
print(cat)
# 不推荐创建对象属性的方式
cat.age = 6
print(cat.age)

print(cat.name)
print(Cat().name)
