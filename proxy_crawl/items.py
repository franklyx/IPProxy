# -*- coding: utf-8 -*-

from scrapy import Item, Field
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst

from sql.mongodb import Mongo
from config import FREE_IP_PROXY, FILTERED_PROXY


class BaseItemLoad(ItemLoader):
    default_output_processor = TakeFirst()


class BaseItem(Item):
    def insert_data(self):
        proxy = Mongo(FREE_IP_PROXY)
        proxy.insert_proxy(dict(self))


class ProxyItem(BaseItem):
    ip = Field()  # ip
    port = Field()  # 端口
    country = Field()  # 国家
    anonymity = Field()  # 匿名性
    source = Field()  # 来源
