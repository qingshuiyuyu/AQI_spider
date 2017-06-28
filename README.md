# 基于scrapy-redis框架构建高密集IO分布式爬虫

## 1.使用scrapy框架中 Spider或CrawlSpider模块构建爬虫

### 1.1 代码参考：AqiCrawlSpider

## 2.构建Scrapy-Redis分布式爬虫

### 2.1 构建过程：

### 1.修改添加settings.py

> 1.\# (必须). 使用了scrapy_redis的去重组件，在redis数据库里做去重
    DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
  2.\#使用了scrapy_redis的调度器，在redis里分配请求
