# -*- coding: utf-8 -*-
import scrapy
import logging
from Myspider.items import TencentItem
import re
logger = logging.getLogger(__name__)

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    def parse(self, response):
        items = response.xpath('//*[contains(@class,"odd") or contains(@class,"even")]')
        for item in items:
            temp = TencentItem()
            temp["name"] = item.xpath("./td[1]/a/text()").extract_first()
            temp["detailLink"] = "http://hr.tencent.com/" + item.xpath("./td[1]/a/@href").extract_first()
            temp["positionInfo"] = item.xpath('./td[2]/text()').extract_first()
            temp["peopleNumber"] = item.xpath('./td[3]/text()').extract_first()
            temp["workLocation"] = item.xpath('./td[4]/text()').extract_first()
            temp["publishTime"] = item.xpath('./td[5]/text()').extract_first()
            yield temp
        # 找到下一页url地址
        # next_url = response.xpath('//*[@id="next"]/@href').extract_first()
        # logger.warning(response.xpath('//*[@id="next"]/@href').extract_first())
        # if next_url != "javascript:;":
        #     next_url = "http://hr.tencent.com/" + next_url
        #     logger.warning(next_url)
        #     yield scrapy.Request(
        #         next_url,
        #         callback=self.parse
        #     )
        now_page = int(re.search(r"\d+", response.url).group(0))
        print("*" * 100)
        if now_page < 30:
            url = re.sub(r"\d+", str(now_page + 10), response.url)
            print("this is next page url:", url)
            print("*" * 100)
            yield scrapy.Request(url, callback=self.parse)
