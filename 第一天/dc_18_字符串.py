str = "hello world"
str1 = "你好'单车'"
print(str)
print(str1)
# 遍历字符串
for c in str1:
    print(c)
# 通过下标获取字符
print(str1[4])
# 获取字符出现的下标
print(str1.index("单"))
# 获取字符串长度
print(len(str1))
# 获取字符出现次数
print(str1.count("你"))
# 判断是否都是空白
str2 = "    \t \n \r"
print(str2.isspace())
# 判断十进制数字
str3 = "10"
print("str3 = %s" % str3)
print(str3.isdecimal())
# 判断unicode
str4 = "\u00b2"
print("str4 = %s" % str4)
print(str4.isdigit())
# 判断中文数字
str5 = "一千零一夜"
print("str5 = %s" % str5)
print(str5.isnumeric())
# 判断字符串开头 (区分大小写)
str5 = "hello world"
print(str5.startswith("hello"))
# 判断字符串结尾 (区分大小写)
print(str5.endswith("world"))
# 替换字符串
str6 = str5.replace("world","python")
print(str5)
print(str6)
# 字符串拆分，返回一个列表
str6 = "我在看世界a世界在看我"
str_list = str6.split("a")
print(str_list)
# 把列表、元组合并成字符串
print("b".join(("打的", "打的")))