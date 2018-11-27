# 定义空元组
tup1 = ()
print(tup1)
# 定义一个元素
tup2 = ("单车",)
print(tup2)
# 获取元素
print(tup2[0])
tup3 = ("张三", "李四", "张三")
# 获取元素的下标
print(tup3.index("李四"))
# 获取元素出现的次数
print(tup3.count("张三"))
# 遍历
for obj in tup3:
    print(obj)
# 格式化字符串，本质是元组
print("名字：%s 名字：%s 名字：%s" % tup3)
# 通过格式化字符串生成一个新字符串
tup_str = "名字：%s 名字：%s 名字：%s" % tup3
print(tup_str)
# 元组转化为列表
arr = list(tup3)
print(arr)
# 列表转化为元组
arr1 = [1, 2, 3, 5, 6]
tup4 = tuple(arr1)
print(tup4)