### 项目简介
   1. 爬取免费的代理IP
   2. 清理不可用的代理IP
   3. 将数据写入到redis数据库
   4. 起flask服务提供接口给程序调用

### 代理IP来源
  * (国外) <https://hidemy.name/en/proxy-list/>
  * (国内) <http://www.ip181.com/>
  * (国内) <http://www.kuaidaili.com/>
  * (国内) <http://m.66ip.cn>
  * (国内) <http://www.xicidaili.com>

### 开发进程
1. 编写爬虫 ☑️
2. 将数据写入数据库mongodb  ☑️
3. 保证ip的实效性，使用request进行验证 ☑️
5. 编写web接口服务 ☑️
6. 优化代码结构，添加日志代码 ☑️
7. 编写docker配置文件 ☑️
8. 正式部署 ☑️

### 其他
1. 为了保证效率默认值爬取http的代
2. 代理的响应时间由清理阶段进行更新
3. 只保留HTTP类型

### ip池更新策略
1. 每隔1小时爬取所有的代理ip
2. 在爬完数据后,将数据进行清理
3. 首先对free代理表进行检验,通过后加入最终proxy表中
4. 然后对最终的proxy表进行检测，删除不行的ip
5. 开始下一次爬虫的时候将上一次的表清空

### scrapydo
    因为execute一次只能引入一个爬虫实例
    所以引用scrapydo


#### 运行方法
1. 运行python crawl.py开启代理池程序
2. 运行python server.py开启服务接口

#### 注意
docker-compose中的volumes 会替换已经编译的镜像中的文件