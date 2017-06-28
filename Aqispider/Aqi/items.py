# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AqiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()#城市
    date = scrapy.Field()#日期
    aqi = scrapy.Field()#等级
    level = scrapy.Field()#等级
    pm2_5 = scrapy.Field()#pm2.5
    pm10 = scrapy.Field()#pm10
    so2 = scrapy.Field()#so2
    co = scrapy.Field()#co
    no2 = scrapy.Field()#二氧化氮
    o3 = scrapy.Field()#臭氧
    rank = scrapy.Field()#排名
