import re
# @之前有4-20位
emails = ["hello@163.com", "12122@126.com", "m473779329393939@163.com"
    ,"1111111111111@16.con", "hello@163.com.com", "hello@163Acom"]
for email in emails:
    ret = re.match(r"^\w{4,20}@163\.com$", email)
    if ret:
        print("变量名 %s 符合要求" % ret.group())
    else:
        print ("不符合要求",email)
