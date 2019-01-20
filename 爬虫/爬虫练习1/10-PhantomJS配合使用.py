from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path="/Users/ming/PycharmProjects/爬虫练习/phantomjs/bin/phantomjs")
driver.get("https://www.baidu.com")
# 设置窗口大小
# driver.set_window_size(1920,1080)
# 最大化窗口
driver.maximize_window()
# 进行页面截屏
driver.save_screenshot("./baidu.png")
# 获取cookie
cookies = driver.get_cookies()
print(cookies)
# 获取html字符串
html = driver.page_source
print(html)
time.sleep(3)
driver.quit()