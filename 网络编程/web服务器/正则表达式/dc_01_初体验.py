import re


names = ["name1", "_name", "2_name", "_name_name"]

for name in names:
    ret = re.match(r"[a-zA-Z]+[\w]*", name)
    if ret:
        print ("变量名 %s 符合要求" % ret.group())
    else:
        print ("不符合要求",name)
