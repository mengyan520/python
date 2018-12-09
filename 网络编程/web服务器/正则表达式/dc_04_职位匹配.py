import re


html_str = "<div><p>职位描述：</p><p>1. 独立完成网站功能点\n的设计和编码工作；</p><p>2. 开发适配 APP 的网页，实现与 APP 的动态交互效果。" \
           "</p><p><br></p><p>任职要求：</p><p>1. 计算机相关专业本科及以上学历；</p><p>2. 熟悉 Python、JS、HTML、CSS 等开发语言；" \
           "</p><p>3. 熟悉 Tornado 等常用 Python 框架，对异步 IO 方式有一定了解；</p><p>4. 熟悉 MySQL、PostgreSQL、Redis 等常" \
           "用数据库及缓存，有一定的数据库优化能力；</p><p>5. " \
           "敢于尝试新的技术和自己不擅长的领域；</p><p>6. 具有较强的自我驱动性，" \
           "追求做事效率；</p><p>7. 熟悉 Git 及相应工作流。</p></div>"
# [^>] 查找除>之外的字符
ret = re.sub(r"<[^>]*>|&nbsp;|\n","",html_str)
print(ret)