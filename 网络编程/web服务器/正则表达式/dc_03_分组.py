import re

html_str = "<h1>hahaha</h1>"

ret = re.match(r"<(\w*)>.*</\1>", html_str)
print(ret.group(1))
print(ret.group())
# 分组起别名
html_str2 = "<h1>hahaha</h1>"

ret = re.match(r"<(?P<p1>\w*)>.*</(?P=p1)>", html_str2)
print(ret.group(1))
print(ret.group())
