import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/54.0.2840.99 Safari/537.36"}
cookieStr = "anonymid=jqtmkfmp93f4ru; depovince=BJ; _r01_=1; ick_login=8c724256-6e32-439d-b02c-9bd4dec763f5; " \
          "first_login_flag=1; ln_uact=15712990611; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; " \
          "jebe_key=fcca816c-19f6-480e-ac24-765951417852%7C0b560e55298d2d7cc790afbf62b0f1e0%7C1547307617534%7C1" \
          "%7C1547307617672; wp_fold=0; jebecookies=ac2d41e0-fcd6-41f2-b293-343c91f3f80e|||||; " \
          "_de=A8A8FF9FB441D4C87187CC9196592CFA; p=9236b6cd5196d36d148481f7e646c8291; " \
          "t=db66bc4427c762e800284771a8fc846a1; societyguester=db66bc4427c762e800284771a8fc846a1; id=969428741; " \
          "xnsid=bd40a6c9; ver=7.0; loginfrom=null"
cookies = {i.split("=")[0]:i.split("=")[1] for i in cookieStr.split(";")}
print(cookies)

# 发送get请求
response = requests.get("http://www.renren.com/327550029/profile", headers=headers,cookies=cookies)

#保存界面
with open("人人网个人界面2.html",'w') as f:
    f.write(response.content.decode())

