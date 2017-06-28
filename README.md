# 基于scrapy-redis框架构建高密集IO分布式爬虫

  
## 爬取内容：全国190多个城市，近三年来的天气质量情况

## 开发环境 
> ubantu-16.04 scrapy
> Scrapy==1.4.0
> scrapy-redis==0.6.3
> scrapyd==1.1.0
> python2.7
> redis==2.10.5





## 1.使用scrapy框架中 Spider或CrawlSpider模块构建爬虫

### 1.1 代码参考：AqiCrawlSpider

## 2.构建Scrapy-Redis分布式爬虫

### 2.1 构建过程：

### 1.修改添加settings.py

> 1.\# (必须). 使用了scrapy_redis的去重组件，在redis数据库里做去重
    DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
  2.\#使用了scrapy_redis的调度器，在redis里分配请求
