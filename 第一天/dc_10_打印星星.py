# 字符串重复操作
i = 0
while i < 5:
    i += 1
    print("*" * i)
# 循环嵌套
i = 0
while i < 5:
    j = 0
    while j <= i:
        print("*",end="")
        j += 1
    print("")
    i += 1
