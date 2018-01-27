#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Created by FrankLyx on 2018/1/18
Desc : 开启flask服务
"""
import json
from flask import Flask

from sql.mongodb import Mongo
from config import FILTERED_PROXY, SERVER_PORT

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/proxy/<int:num>')
def get_ips(num=1):
    proxy = Mongo(FILTERED_PROXY)
    proxys = proxy.obtain_proxy(num)
    return json.dumps(proxys)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=SERVER_PORT)
