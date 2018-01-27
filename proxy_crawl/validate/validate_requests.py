#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Created by FrankLyx on 2018/1/22
Desc :通过request检验代理
"""
import os
import sys
import logging

import requests

sys.path.append(os.path.dirname(os.path.abspath("__file__")))

from sql.mongodb import Mongo
from config import FREE_IP_PROXY, FILTERED_PROXY


class Validate:
    def __init__(self):
        self.header = {}
        self.urls = []
        self.timeout = 4  # 时间间隔
        self.tables = [FILTERED_PROXY, FREE_IP_PROXY]

    def start_requests(self):
        for table in self.tables:
            self.proxy = Mongo(table)
            proxys = self.proxy.select_proxy()
            for proxy in proxys:
                for url in self.urls:
                    logging.info("Validate:" + "URL:" + url + "Proxy:" + proxy)
                    proxies = {'http': '%s:%s' % (proxy.get("ip"), proxy.get("port"))}
                    try:
                        requests.get(url, proxies=proxies, timeout=self.timeout)
                        self.success_parse(proxy)
                    except:
                        self.error_parse(proxy)

    def success_parse(self, proxy):
        logging.info("Qualified:" + proxy)

    def error_parse(self, proxy):
        # 响应失败
        self.proxy.delete_with_ip(proxy.get("ip"))
        logging.info("Unqualified:" + proxy + "it is so slowly,will deleted")

    def close(self):
        # 将爬取的ip加入到最终的ip表中
        pass_proxys = Mongo(FREE_IP_PROXY).select_proxy()
        for pass_proxy in pass_proxys:
            logging.info("Join:" + pass_proxy + "will join filtered_collection")
            Mongo(FILTERED_PROXY).insert_proxy(pass_proxy)


if __name__ == "__main__":
    va = Validate()
    va.start_requests()
    va.close()
