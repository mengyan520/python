def input_pwd():
    pwd = input("请输入密码：")
    if len(pwd) >= 8:
        return pwd
    print("主动抛出异常")
    ex = Exception("密码长度不够")
    raise ex

try:
    input_pwd()
except Exception as result:
    print(result)