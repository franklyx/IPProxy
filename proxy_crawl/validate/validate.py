#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Created by FrankLyx on 2018/1/22
Desc :spider基类
"""
import time
import logging

from scrapy import Request
from scrapy import Spider

from sql.mongodb import Mongo
from config import FREE_IP_PROXY, FILTERED_PROXY


class Validate(Spider):
    name = 'base'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.header = {}
        self.urls = []
        self.timeout = 7  # 时间间隔
        self.proxy = None
        self.tables = [FILTERED_PROXY, FREE_IP_PROXY]

    def start_requests(self):
        for table in self.tables:
            self.proxy = Mongo(table)
            proxys = self.proxy.select_proxy()
            for proxy in proxys:
                for url in self.urls:
                    logging.info("Validate:" + "URL:" + url + "Proxy:" + proxy)
                    yield Request(url=url,
                                  meta={
                                      'proxy': 'http://%s:%s' % (proxy.get("ip"), proxy.get("port")),
                                      'download_timeout': self.timeout,
                                  },
                                  priority=0,
                                  headers=self.header,
                                  dont_filter=True,
                                  callback=self.success_parse,
                                  errback=self.error_parse)

    def success_parse(self, response):
        # 响应成功
        proxy = response.meta.get('proxy_info')
        speed = time.time() - response.meta.get('cur_time')
        if speed >= self.timeout:
            # 超时删除改ip
            logging.info("Unqualified:" + proxy + "it is so slowly,will deleted")
            self.proxy.delete_with_ip(proxy.get("ip", ""))
        else:
            logging.info("Qualified:" + proxy)

    def error_parse(self, failure):
        # 响应超时
        request = failure.request
        proxy = request.meta.get('proxy_info')
        proxy.https = request.meta.get('https')
        self.proxy.delete_with_ip(proxy.get("ip", ""))
        logging.info("Unqualified:" + proxy + "it is error,will deleted")

    def close(spider, reason):
        # 将免费ip中的前缀加入最终的代理池中
        pass
