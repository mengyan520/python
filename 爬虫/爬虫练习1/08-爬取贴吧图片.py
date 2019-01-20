import requests
import json
from lxml import etree


class Tieba_Spider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.part_url = "https://tieba.baidu.com"
        self.headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 ("
                                      "KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
        self.start_url = "https://tieba.baidu.com/mo/q/m?word=" + tieba_name + "&page_from_search=index&tn6=bdISP&tn4" \
                                                                               "=bdKSW&tn7=bdPSB&lm=16842752&lp=6093" \
                                                                               "&sub4=%E8%BF%9B%E5%90%A7&pn=0 "
        response = requests.get("https://tieba.baidu.com/p/6007260038?lp=5028&mo_device=1&is_jingpost=0",
                                headers=self.headers)
        html = etree.HTML(response.content.decode())
        imgs = html.xpath("//img/@src")
        print(imgs)

    def parse_url(self, url):  # 发送请求，获取响应
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, html_str):  # 提取数据
        html = etree.HTML(html_str)
        li_list = html.xpath("//li[contains(@class,'tl_shadow')]")
        content_list = []
        for li in li_list:
            temp = dict(
                title=li.xpath("./a/div[@class='ti_title']/span/text()")[0] if len(li.xpath("./a/div[@class='ti_title"
                                                                                            "']/span/text()")) > 0 else
                None,
                href=self.part_url + li.xpath("./a/@href")[0] if len(li.xpath("./a/@href")) > 0 else None,
                img_list=self.get_image_list(
                    self.part_url + li.xpath("./a/@href")[0] if len(li.xpath("./a/@href")) > 0 else None)
            )
            content_list.append(temp)
        return {"content": content_list}

    def get_image_list(self, detail_url):  # 获取帖子中所有图片
        if detail_url == 'https://tieba.baidu.comjavascript:;':
            return None
        # 3.2 请求列表页的url地址，获取详情页的第一页
        print(detail_url)
        detail_html_str = self.parse_url(detail_url)
        detail_html = etree.HTML(detail_html_str)
        # 3.3 提取详情页的第一页道德图片，提取下一页的第一页
        img_list = detail_html.xpath("//img[@class='BDE_Image']/@src")
        # 3.4  请求详情页下一页的地址，进入循环3.2-3.4
        return img_list

    def save_content_list(self, content_list):
        file_path = self.tieba_name + ".json"
        with open(file_path, 'w') as f:
            f.write(json.dumps(content_list, ensure_ascii=False, indent=2))

    def run(self):
        # 1.start_url
        # 2.发送请求，获取响应
        html_str = self.parse_url(self.start_url)
        # print(html_str)
        # 3.提取数据，提取下一页的url地址
        conten_list = self.get_content_list(html_str)
        # 4.保存数据
        self.save_content_list(conten_list)
        # 5.请求下一页的url地址，进入循环2-5


if __name__ == '__main__':
    tieba = Tieba_Spider("lol")
    # tieba.run()
