class Animal:
    def eat(self):
        print("动物会吃")


class Dog(Animal):
    def sound(self):
        print("汪汪叫")


dog = Dog()
dog.eat()
dog.sound()
