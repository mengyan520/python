age = int(input("请输入你的年龄："))
if age >= 18:
    print("成年")
elif age < 0:
    print('未出生')
else:
    print("未成年")