from selenium import webdriver
import time
# 实例化一个浏览器对象
driver = webdriver.Chrome()
# 发送请求
driver.get("https://douban.com")
# 元素定位的方法,只有inpou标签调用send_keys有效
driver.find_element_by_id("form_email").send_keys("15712990611")
driver.find_element_by_id("form_password").send_keys("feiyang521")
time.sleep(5)
# 标签点击事件
driver.find_element_by_class_name("bn-submit").click()
cookies = {i["name"]:i["value"] for i in driver.get_cookies()}
print(cookies)
time.sleep(3)
# 退出浏览器,每次执行都会创建一个浏览器对象，需要调用退出，节省内存（尤其和PhantomJS配合使用的时候）
driver.quit()
