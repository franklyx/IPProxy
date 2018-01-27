#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Created by FrankLyx on 2018/1/19
Desc : 写入mongo
"""
import logging
from datetime import datetime

from config import DB_CONFIG, DATABASE
from pymongo import MongoClient


class Mongo:
    def __init__(self, collection):
        self.client = MongoClient("mongodb://{user}:{password}@{host}:{port}/{db}".format(**DB_CONFIG, db=DATABASE))
        self.collection = collection
        self.db = self.client.ipproxy
        self.proxy = self.db[collection]
        self.create_index()

    def create_index(self):
        # 为字段创建索引
        self.proxy.create_index("ip", unique=True)

    def insert_proxy(self, proxy):
        try:
            proxy["speed"] = 0
            proxy["type"] = "http"
            proxy["add_time"] = datetime.utcnow()
            return self.proxy.insert(proxy)
        except:
            # 处理ip已存在问题
            logging.info("%s existing" % proxy)

    def select_proxy(self, **kwargs):
        res = self.proxy.find(kwargs)
        return list(res)

    def delete_with_ip(self, ip):
        return self.proxy.delete_one({"ip": ip})

    def update_proxy(self, proxy):
        return self.proxy.update_one({"ip": proxy.get("ip")}, {"$set": proxy})

    def obtain_proxy(self, num):
        # 返回num个代理
        res = []

        proxys = self.proxy.aggregate([
            {"$sample": {"size": int(num)}}
        ])
        for proxy in proxys or []:
            ip = "{type}://{ip}:{port}".format(**proxy)
            res.append(ip)
        return res

    def drop_collections(self):
        res = self.db.drop_collection(self.collection)
        logging.info("will delete collection %s" % self.collection)
        return res


if __name__ == "__main__":
    pass
