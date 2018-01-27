#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Created by FrankLyx on 2018/1/18
Desc : http://www.xicidaili.com
"""

from proxy_crawl.spiders.basespider import BaseSpider
from proxy_crawl.items import ProxyItem, BaseItemLoad


class XiCiDaiLi(BaseSpider):
    name = "xici"

    def __init__(self, source=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.5',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'www.xicidaili.com',
            'If-None-Match': 'W/"cb655e834a031d9237e3c33f3499bd34"',
            'Upgrade-Insecure-Requests': '1',
        }
        self.urls = ["http://www.xicidaili.com/nn/%s" % i for i in range(1, 10)]

    def parse_page(self, response):
        proxy_list = response.css("#ip_list tbody tr:not(:nth_child(1))")
        for proxy in proxy_list:
            item_load = BaseItemLoad(item=ProxyItem(), selector=proxy)
            item_load.add_xpath("ip", ".//td[2]/text()")
            item_load.add_xpath("port", ".//td[3]/text()")
            item_load.add_xpath("country", ".//td[4]/a/text()")
            item_load.add_xpath("anonymity", ".//td[5]/text()")
            yield item_load.load_item()
