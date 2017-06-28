# -*- coding: utf-8 -*-
import scrapy
from Aqi.items import AqiItem
from scrapy_redis.spiders import RedisSpider

class AqiSpider(RedisSpider):
    name = 'aqi'
    allowed_domains = ['aqistudy.cn']

    #start_urls = ['https://www.aqistudy.cn/historydata/']
    redis_key = 'aqi:start_urls'
    baseURL = 'https://www.aqistudy.cn/historydata/'

    #提取每个城市的链接
    def parse(self, response):
        city_list = response.xpath("//div[@class='all']//a/@href").extract()

        for city in city_list:
            url = self.baseURL + city
            yield scrapy.Request(url,callback=self.parse_month)
    def parse_month(self,response):
        month_list = response.xpath("//td[@align='center']//a/@href").extract()

        for month in month_list:
            url = self.baseURL + month
            yield scrapy.Request(url,callback=self.parse_day)

    def parse_day(self,response):
        day_list = response.xpath("//table[@class='table table-condensed table-bordered table-striped table-hover table-responsive']//tr")
        city = response.xpath("//div[@class='form-group']/input/@value").extract()
        #去处表头
        day_list.pop(0)
        for day in day_list:
            item = AqiItem()

            item['city'] = city
            item['date'] = day.xpath("./td[1]/text()").extract_first() or '0'
            item['aqi'] = day.xpath("./td[2]/text()").extract_first() or '0'
            item['level'] = day.xpath("./td[3]//text()").extract_first() or '0'
            item['pm2_5'] = day.xpath("./td[4]/text()").extract_first() or '0'
            item['pm10'] = day.xpath("./td[5]/text()").extract_first() or '0'
            item['so2'] = day.xpath("./td[6]/text()").extract_first() or '0'
            item['co'] = day.xpath("./td[7]/text()").extract_first() or '0'
            item['no2'] = day.xpath("./td[8]/text()").extract_first() or '0'
            item['o3'] = day.xpath("./td[9]/text()").extract_first() or '0'
            item['rank'] = day.xpath("./td[10]/text()").extract_first() or '0'

            yield item





