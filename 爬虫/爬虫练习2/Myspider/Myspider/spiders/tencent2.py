# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Tencent2Spider(CrawlSpider):
    name = 'tencent2'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    rules = (
        Rule(LinkExtractor(allow=r'position\.php\?&start=\d+#a'),callback='parse_item',follow=True),
    )

    def parse_item(self, response):
        items = response.xpath('//*[contains(@class,"odd") or contains(@class,"even")]')
        for item in items:
            temp = {}
            temp["title"] = item.xpath("./td[1]/a/text()").extract_first()
            temp["href"] = "http://hr.tencent.com/" + item.xpath("./td[1]/a/@href").extract_first()
            yield scrapy.Request(
                temp["href"],
                callback=self.parse_detail,
                meta={"item":temp}
            )
        # return item

    def parse_detail(self, response):
        item = response.meta["item"]
        item["aquire"] = response.xpath("//div[text()='工作要求：']/../ul/li/text()").extract()
        print(item)
