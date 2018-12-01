class Person(object):
    def eat(self):
        print("人会吃饭")
    def __getAge(self):
        print(18)

class Man():
    def work(self):
        print("男人工作")


class Student(Person, Man):
    # 子类重写
    def eat(self):
        # 调用父类方法
        super().eat()
        # 也可直接通过父类调用，不推荐，因为类名一旦改变，也需要改变
        Person.eat(self)
        print("学生吃饭")
    def study(self):
        print("学生学习")

student = Student()
student.eat()
student.work()
student.study()
print(Student.__mro__)
print(dir(Person()))