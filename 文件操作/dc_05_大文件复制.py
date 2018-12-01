file_read = open("README")
file_write = open("README[大复制]", "w")
while True:
    txt = file_read.readline()
    if not txt:
        break
    file_write.writelines(txt)
file_read.close()
file_write.close()