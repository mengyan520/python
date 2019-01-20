# -*- coding: utf-8 -*-
import scrapy
from Myspider.items import YGItem

class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):
        tr_list = response.xpath("//div[@class='greyframe']/table[2]//table/tr")
        for tr in tr_list:
            item = YGItem()
            item["ID"] = tr.xpath("./td/text()").extract_first()
            item["title"] = tr.xpath("./td[2]/a[2]/@title").extract_first()
            item["href"] = tr.xpath("./td[2]/a[2]/@href").extract_first()
            item["publish_date"] = tr.xpath("./td[last()]/text()").extract_first()
            yield scrapy.Request(
                item["href"],
                callback=self.parse_detail,
                meta={"item": item}
            )

    def parse_detail(self, response):
        """处理详情页"""
        item = response.meta["item"]
        item["content"] = response.xpath("//div[@class='wzy1']/table[2]//tr[1]/td//text()").extract()
        item["content_img"] = response.xpath("//div[@class='wzy1']//img/@src").extract()
        item["content_img"] = ["http://wz.sun0769.com/" + i for i in item["content_img"]]
        yield item
