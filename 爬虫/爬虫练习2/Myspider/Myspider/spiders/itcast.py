# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # 处理url地址对应的响应
        rets = response.xpath("//div[@class='tea_con']//li")
        for li in rets:
            item = {}
            item["name"] = li.xpath(".//h3/text()").extract_first()
            item["title"] = li.xpath(".//h4/text()").extract_first()
            item["prifile"] = li.xpath("./div/p/text()").extract_first()
            logger.warning(item)
            yield item