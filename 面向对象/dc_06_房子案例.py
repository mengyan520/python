class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s,占地面积：%.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        # 家具列表
        self.item_list = []

    def addItem(self, item):
        if item.area > self.free_area:
            print("无法添加")
            return
        self.item_list.append(item.name)
        self.free_area -= item.area

    def __str__(self):
        return ("户型：%s 总面积：%.2f 剩余面积：%.2f 家具：%s" %
                (self.house_type, self.area, self.free_area, self.item_list))


house1 = House("别墅", 50)
item1 = HouseItem("席梦思", 40)
item2 = HouseItem("板凳", 5)
house1.addItem(item1)
house1.addItem(item2)
print(house1)
