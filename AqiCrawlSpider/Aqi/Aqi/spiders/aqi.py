# -*- coding: utf-8 -*-
import scrapy
from Aqi.items import AqiItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AqiSpider(CrawlSpider):
    name = 'aqi'
    allowed_domains = ['aqistudy.cn']
    start_urls = ['https://www.aqistudy.cn/historydata/']

    rules = (
        Rule(LinkExtractor(allow=r'monthdata\.+'), follow=True),
        Rule(LinkExtractor(allow=r'month=\d+'), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        day_list = response.xpath(
            "//table[@class='table table-condensed table-bordered table-striped table-hover table-responsive']//tr")
        city = response.xpath("//div[@class='form-group']/input/@value").extract()
        # 去处表头
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
