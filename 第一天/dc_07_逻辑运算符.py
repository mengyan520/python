age = int(input('请输入你的年龄：'))
if age > 20 or age > 18:
    print("你该结婚了")
else:
    print("社会人")
if 0 < age < 18:
    print("学生")
if age > 0 and age < 18:
    print("学生")
if not not age :
    print("数字")