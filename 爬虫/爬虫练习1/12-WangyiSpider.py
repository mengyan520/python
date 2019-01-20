from selenium import webdriver
import time


class WangYiSpider:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def run(self):
        self.driver.get("https://music.163.com")
        # 点击歌单
        self.driver.find_element_by_xpath('//*[@id="g_nav2"]/div/ul/li[3]/a/em').click();
        time.sleep(3)
        # 页面跳转 iframe
        self.driver.switch_to_frame("g_iframe")
        # 点击选择分类
        self.driver.find_element_by_xpath('//*[@id="cateToggleLink"]').click()

        # 获取歌单大分类
        fengge = self.driver.find_elements_by_xpath("//dl[@class='f-cb']/dt")
        for i in fengge:
            print(i.text)
            names = i.find_elements_by_xpath("../dd/a")
            for n in names:
                print(n.text)

    def __del__(self):
        self.driver.quit()


if __name__ == '__main__':
    wy = WangYiSpider()
    wy.run()
    while True:
        pass
