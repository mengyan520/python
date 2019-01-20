# -*- coding: utf-8 -*-
import json
import re
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 保存数据库
from pymongo import MongoClient
from Myspider.items import TencentItem
from Myspider.items import YGItem

client = MongoClient()
collection = client["tencent"]["hr"]


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        if spider.name == "itcast":
            with open("teacher.txt", 'a') as f:
                json.dump(item, f, ensure_ascii=False, indent=2)
        return item


class MyspiderPipeline2(object):
    def process_item(self, item, spider):
        if spider.name == "tencent":
            # 插入数据
            if isinstance(item, TencentItem):
                item = dict(item)
            collection.insert(item)
        return item


class MyspiderPipeline3(object):
    def process_item(self, item, spider):
        if spider.name == "yg":
            item["content"] = self.process_content(item["content"])
            if isinstance(item, YGItem):
                with open("yg.txt", 'a') as f:
                    json.dump(dict(item), f, ensure_ascii=False, indent=2)

        return item

    def process_content(self, content):
        content = [re.sub(r"\xa0|\s", "", i) for i in content]
        # 去除列表中空字符串
        content = [i for i in content if len(i) > 0]
        return content
