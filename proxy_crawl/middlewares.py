# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from fake_useragent import UserAgent
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware

from utils.ip_proxy import Get_Ip


class ProxyCrawlSpiderMiddleware(object):
    pass


class RandomUserAgentMiddlware(UserAgentMiddleware):
    # 随机更换user-agent
    def __init__(self, crawler):
        super(RandomUserAgentMiddlware, self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get("RANDOM_UA_TYPE", "random")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        def get_ua():
            return getattr(self.ua, self.ua_type)

        request.headers.setdefault('User-Agent', get_ua())


class RandomProxyMiddleware(HttpProxyMiddleware):
    # 动态设置ip代理
    def process_request(self, request, spider):
        get_ip = Get_Ip()
        request.meta["proxy"] = get_ip.get_random_ip()
