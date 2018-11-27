dic = {"name": "单车",
       "age": 18
       }
print(dic)
# 取值
print(dic["name"])
# 增加元素
dic["height"] = 1.75
print(dic)
# 更改元素
dic["height"] = 1.85
print(dic)
# 删除元素
dic.pop("height")
print(dic)
# 合并字典
dic1 = {"age":26,"weight":130}
dic.update(dic1)
print(dic)
# 清空字典
dic.clear()
print(dic)
# 遍历
for k in dic1:
    print(k)
    print(dic1[k])
