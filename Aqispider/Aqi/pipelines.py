# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class AqiPipeline(object):
    def open_spider(self,spider):
        self.f = open('aqi.json','w')
    def process_item(self, item, spider):
        conment = json.dumps(dict(item),ensure_ascii=False)+',\n'
        self.f.write(conment.encode("utf-8"))
        return item
    def close_spider(self,spider):
        self.f.close()