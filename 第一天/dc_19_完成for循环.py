arr = [1, 2, 3, 4, 5]
for index in arr:
    print(index)
else:
    print("遍历完成")
for index in arr:
    print(index)
    if index == 4:
        break
else:
    print("不会走")