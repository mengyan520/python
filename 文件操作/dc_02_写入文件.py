# 打开
file = open("README","a")
# 写入文件
file.write("\n我是被写入的")
# 关闭
file.close()
file1 = open("README")
txt = file1.read()
# 关闭
file1.close()
print(txt)