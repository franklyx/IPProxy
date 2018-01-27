#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Created by FrankLyx on 2018/1/18
Desc : http://www.ip181.com/
"""

from proxy_crawl.spiders.basespider import BaseSpider
from proxy_crawl.items import ProxyItem, BaseItemLoad


class IP181(BaseSpider):
    name = "ip181"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.urls = ["http://www.ip181.com/"]
        self.header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Host': 'www.ip181.com',
            'Upgrade-Insecure-Requests': '1',
        }
        self.init()

    def parse_page(self, response):
        proxy_list = response.css(".ctable tbody tr:not(:nth_child(1))")
        for proxy in proxy_list:
            item_load = BaseItemLoad(item=ProxyItem(), selector=proxy)
            item_load.add_xpath("ip", ".//td[1]/text()")
            item_load.add_xpath("port", ".//td[2]/text()")
            item_load.add_xpath("country", ".//td[6]/text()")
            item_load.add_xpath("anonymity", ".//td[3]/text()")

            yield item_load.load_item()
