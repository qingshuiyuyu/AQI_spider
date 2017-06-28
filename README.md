

# 基于scrapy-redis框架构建高密集IO分布式爬虫  
  
  

## 爬取内容：全国190多个城市，近三年天气质量情况,一共24万余条数据，存在Aqispider/data/aqi.json里面  
  

## web:https://www.aqistudy.cn/historydata/

## 开发环境: 
####  **ubantu-16.04 scrapy**
####  **Scrapy==1.4.0**
#### **scrapy-redis==0.6.3**
#### **scrapyd==1.1.0**  
#### **python2.7**  
#### **redis==2.10.5**
----------
## 1.使用scrapy框架中 Spider或CrawlSpider模块构建爬虫

###1.1 代码参考：AqiCrawlSpider 

## 2.构建Scrapy-Redis分布式爬虫

### 2.1 构建过程：

### 1.修改添加settings.py

**1.\# (必须). 使用了scrapy_redis的去重组件，在redis数据库里做去重**  
> 
	DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  


**2 使用了scrapy_redis的调度器，在redis里分配请求**  
>
    SCHEDULER = "scrapy_redis.scheduler.Scheduler"

**3 在redis中保持scrapy-redis用到的各个队列，从而允许暂停和暂停后恢复，也就是不清理redis queues**  
>
	SCHEDULER_PERSIST = True  

**4. 通过配置RedisPipeline将item写入key为 spider.name : items 的redis的list中，供后面的分布式处理item**  
>
	ITEM_PIPELINES = {
    # 'AQI.pipelines.AqiJsonPipeline': 200,
    'scrapy_redis.pipelines.RedisPipeline': 100
	}

**5.指定redis数据库的连接参数**  
>
	REDIS_HOST = '127.0.0.1'#此处填master主机redis地址
	REDIS_PORT = 6379

  
### 2.修改 spiders/aqi.py

**在spiders目录下增加aqi.py文件编写我们的爬虫，使其具有分布式：**
>
	# 1. 导入RedisSpider类，不使用Spider
	from scrapy_redis.spiders import RedisSpider
>	
	#2.导入RedisSpider类，不使用Spider
	class AqiSpider(RedisSpider):
    	name = 'aqi'
    	allowed_domains = ['aqistudy.cn']
    	baseURL = "https://www.aqistudy.cn/historydata/"
>	
    # 3. 取消start_urls，增加redis-key，接受从Redis数据库里的指令    
    #start_urls = [baseURL]
    redis_key = 'aqi:start_urls'

### **3.分布式爬虫执行**


#### 3.1在Master端启动redis-server：

	sudo redis-server /etc/redis/redis.conf

#### 3.2在Slave端spiders目录下分别启动爬虫，不分先后：

	scrapy runspider aqi.py

#### 3.3所有Slaver端将处于等待指令状态，在Master端的redis-cli里push一个redis_key

	redis-cli> lpush aqi:start_urls https://www.aqistudy.cn/historydata/

#### 3.4爬虫启动，所有Slaver端将开始爬取数据，数据将保存在Redis数据库中，并共享Redis数据库的请求队列、请求指纹集合和数据队列。


