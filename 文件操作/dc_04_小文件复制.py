# 读取源文件， 写入目标文件

file_read = open("README")
file_write = open("README[复制]", "w")

txt = file_read.read()
file_write.write(txt)
file_read.close()
file_write.close()
