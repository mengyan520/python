class Gun:
    def __init__(self, name):
        self.name = name
        self.bullet = 0

    def add_bullet(self):
        self.bullet += 30
        print("添加30发子弹")

    def shoot(self):
        if self.bullet <= 0:
            print("没有子弹")
            return
        self.bullet -= 10
        print("开枪,减少10发子弹，剩余%d发子弹" % self.bullet)


class Solider:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def free(self):
        self.model.shoot()


ak = Gun("AK47")
ak.add_bullet()
person = Solider("单车", ak)
person.free()
