#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Created by FrankLyx on 2018/1/22
Desc :
"""
import logging
from datetime import datetime

from scrapy import Spider
from scrapy.http import Request


class BaseSpider(Spider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.header = {}
        self.urls = []
        self.timeout = 10
        self.meta = {}

    def init(self):
        self.meta = {
            'download_timeout': self.timeout,
        }

    def start_requests(self):
        for url in self.urls:
            yield Request(url=url,
                          meta=self.meta,
                          headers=self.header,
                          callback=self.parse_page,
                          errback=self.error_parse)

    def parse_page(self, response):
        pass

    def error_parse(self, failure):
        pass

    def close(spider, reason):
        pass
