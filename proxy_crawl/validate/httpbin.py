#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Created by FrankLyx on 2018/1/22
Desc : 基本http验证
"""
# from proxy_crawl.validate.validate import Validate
from proxy_crawl.validate.validate_requests import Validate


class HttpBin(Validate):
    name = 'httpbin'

    def __init__(self):
        super().__init__()
        self.urls = [
            'https://httpbin.org/get?show_env=1',
        ]
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Host": "httpbin.org",
            "Upgrade-Insecure-Requests": "1",
        }
