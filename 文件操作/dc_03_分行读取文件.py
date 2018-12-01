file1 = open("README")
while True:
    text = file1.readline()
    if not text:
        break
    print(text)
# 关闭
file1.close()