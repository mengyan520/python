import requests

# 创建session对象
ssion = requests.session()
# 发送post请求,存储cookie
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/54.0.2840.99 Safari/537.36"}
data = {"email": "15712990611", "password": "feiyang521"}
ssion.post("http://www.renren.com/PLogin.do", data=data, headers=headers)
# 发送get请求
response = ssion.get("http://www.renren.com/327550029/profile", headers=headers)

# 保存界面
with open("人人网个人界面.html", 'w') as f:
    f.write(response.content.decode())
