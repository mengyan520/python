arr = [1, 2, 3, 4, 5]
print(arr)
# 获取元素第一次出现的下标
print(arr.index(4))
# 修改元素
arr[2] = 6
print(arr)
# 在列表最后添加元素
arr.append(10)
print(arr)
# 在指定下标插入元素
arr.insert(1, 20)
print(arr)
# 在列表内部插入另一个列表
arr2 = [55, 66, 77]
arr.extend(arr2)
print(arr)
# 删除指定元素
arr.remove(5)
print(arr)
# 移除下标元素，默认移除末尾
arr.pop(2)
print(arr)
# 清空列表
arr.clear()
print(arr)
# 删除指定下标元素
del arr2[0]
# 使用del删除内存中的变量
del arr2
# 获取列表长度
arr3 = [1, 2, 3, 4, 5, 5]
print(len(arr3))
# 统计列表某个元素出现的次数
print(arr3.count(5))
# 列表升序
arr4 = [5, 6, 4, 3, 2, 1]
arr4.sort()
print(arr4)
# 降序
arr4.sort(reverse=True)
print(arr4)
# 反转
arr4.reverse()
print(arr4)
# 列表遍历
arr5 = ["张三","李四","豆腐","辅助"]
for obj in arr5:
    print(obj)
