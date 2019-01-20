# -*- coding: utf-8 -*-
import scrapy
import re


class LoginrenrenSpider(scrapy.Spider):
    name = 'logInrenren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/969428741/profile']

    def start_requests(self):
        cookies = "anonymid=jqtmkfmp93f4ru; _r01_=1; ln_uact=15712990611; " \
                  "ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; " \
                  "jebe_key=fcca816c-19f6-480e-ac24-765951417852%7C0b560e55298d2d7cc790afbf62b0f1e0%7C1547307617534" \
                  "%7C1%7C1547307617672; _de=A8A8FF9FB441D4C87187CC9196592CFA; _ga=GA1.2.1223460954.1547345945; " \
                  "depovince=GW; jebecookies=a6fedf99-0855-4403-9655-09a03ecbbfb8|||||; " \
                  "JSESSIONID=abcsp5snxDRyXgsb-UOHw; ick_login=ff750701-8c34-4a79-bf3c-9c12d96a2186; " \
                  "p=d6193a4bb8d09331c4c81dc7402528451; first_login_flag=1; t=cb4e3ae466a75f9551e8c0909300a0b41; " \
                  "societyguester=cb4e3ae466a75f9551e8c0909300a0b41; id=969428741; xnsid=97440524; ver=7.0; " \
                  "loginfrom=null; wp_fold=0; " \
                  "jebe_key=fcca816c-19f6-480e-ac24-765951417852%7C0b560e55298d2d7cc790afbf62b0f1e0%7C1547307617534" \
                  "%7C1%7C1547945455912; ch_id=10013; _gid=GA1.2.1036254919.1547945503 "
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split(";")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        print(re.findall("马鸣", response.body.decode()))
        yield scrapy.Request(
            "http://www.renren.com/969428741/profile?v=info_timeline",
            callback=self.parse_detial
        )

    def parse_detial(self, response):
        print(re.findall("马鸣", response.body.decode()))
