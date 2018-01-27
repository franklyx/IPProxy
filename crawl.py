#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Created by FrankLyx on 2018/1/18
Desc : 爬虫启动
"""
import time
import logging

import os
import scrapydo

from sql.mongodb import Mongo
from config import FREE_IP_PROXY
from proxy_crawl.spiders.ip181 import IP181
from proxy_crawl.spiders.sixip import SixIp
from proxy_crawl.spiders.kuaidaili import KuaiDaiLi
from proxy_crawl.spiders.xicidaili import XiCiDaiLi
from proxy_crawl.validate.baidu import Baidu
from proxy_crawl.validate.httpbin import HttpBin
from config import LOG_FILENAME, LOG_FORMAT, LOG_LEVEL, LOG_PATH

scrapydo.setup()


def init_log():
    # 创建日志文件夹
    if not os.path.exists(LOG_PATH):
        os.mkdir(LOG_PATH)

    logging.basicConfig(
        filename=LOG_FILENAME,
        format=LOG_FORMAT,
        level=LOG_LEVEL
    )


if __name__ == "__main__":
    # 初始化日志
    init_log()
    logging.info("Begin proxy crawl")
    spiders = [IP181, SixIp, KuaiDaiLi, XiCiDaiLi]
    validates = [Baidu, HttpBin]

    while True:
        ipproxy = Mongo(FREE_IP_PROXY)
        ipproxy.drop_collections()
        # 爬取代理
        for spider in spiders:
            scrapydo.run_spider(spider)
        # 校验代理
        for validate in validates:
            va = validate()
            va.start_requests()
            va.close()

        time.sleep(7200)
