#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Created by FrankLyx on 2018/1/18
Desc : https://hidemy.name/en/proxy-list/
"""
from proxy_crawl.spiders.basespider import BaseSpider
from proxy_crawl.items import ProxyItem, BaseItemLoad


class HideMy(BaseSpider):
    name = "hidemy"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.urls = ["https://hidemy.name/en/proxy-list/?start=%s#list" % i * 64 for i in range(10)]
        self.header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Host': 'hidemy.name',
            'Referer': 'https://hidemy.name/en/proxy-list/?start=0',
            'Upgrade-Insecure-Requests': '1',
        }

    def parse(self, response):
        proxy_list = response.css(".proxy__t tbody tr:not(:nth_child(1))")
        for proxy in proxy_list:
            item_load = BaseItemLoad(item=ProxyItem(), selector=proxy)
            item_load.add_xpath("ip", ".//td[1]/text()")
            item_load.add_xpath("port", ".//td[2]/text()")
            item_load.add_xpath("country", ".//td[3]/text()")
            item_load.add_xpath("anonymity", ".//td[6]/text()")

            yield item_load.load_item()
