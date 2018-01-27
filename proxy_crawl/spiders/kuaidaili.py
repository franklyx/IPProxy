#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Created by FrankLyx on 2018/1/18
Desc : https://www.kuaidaili.com/free/inha/
"""

from proxy_crawl.spiders.basespider import BaseSpider
from proxy_crawl.items import ProxyItem, BaseItemLoad


class KuaiDaiLi(BaseSpider):
    name = "kuaidai"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.urls = ["https://www.kuaidaili.com/free/inha/%s/" % i for i in range(1, 10)]
        self.header = {
            'Host': 'www.kuaidaili.com',
            'Upgrade-Insecure-Requests': '1',
        }
        self.init()

    def parse_page(self, response):
        proxy_list = response.css("#list tbody tr:not(:nth_child(1))")
        for proxy in proxy_list:
            item_load = BaseItemLoad(item=ProxyItem(), selector=proxy)
            item_load.add_xpath("ip", ".//td[1]/text()")
            item_load.add_xpath("port", ".//td[2]/text()")
            item_load.add_xpath("country", ".//td[5]/text()")
            item_load.add_xpath("anonymity", ".//td[3]/text()")

            yield item_load.load_item()
