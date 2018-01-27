#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Created by FrankLyx on 2018/1/19
Desc :
"""
from sql.mongodb import Mongo
from config import FILTERED_PROXY


class Get_Ip:
    def get_random_ip(self):
        proxy = Mongo(FILTERED_PROXY).obtain_fasted_proxy()
        return proxy
