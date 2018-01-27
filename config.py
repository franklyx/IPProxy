#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Created by FrankLyx on 2018/1/19
Desc : 文件配置
"""

import os
import logging

DB_CONFIG = {
    'host': '10.9.36.126',
    'port': "27017",
    'user': 'frank',
    'password': 'frank',
}

DATABASE = "ipproxy"
FREE_IP_PROXY = "free_ip_proxy"
FILTERED_PROXY = "filtered_proxy"
SERVER_PORT = 5555

# 设置日志
LOG_PATH = os.path.join(os.path.dirname(os.path.abspath("__file__")), "logs")
LOG_FILENAME = os.path.join(LOG_PATH, "ip_proxy.txt")
LOG_FORMAT = '%(levelname)s %(asctime)s: %(message)s'
LOG_LEVEL = logging.INFO
