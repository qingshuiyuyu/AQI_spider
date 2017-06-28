# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exporters import CsvItemExporter
class AqiPipeline(object):
    def open_spider(self,spider):
        self.f = open('aqi.json','w')
    def process_item(self, item, spider):
        conment = json.dumps(dict(item),ensure_ascii=False)+',\n'
        self.f.write(conment.encode("utf-8"))
        return item
    def close_spider(self,spider):
        self.f.close()

class AqiCSVPipeline(object):
    def open_spider(self, spider):
        # 创建csv文件对象，拥有写权限
        self.csv = open("aqi.csv", "w")
        # 查创建一个Csv文件读写对象，参数是csv文件对象
        self.csvexporter = CsvItemExporter(self.csv)
        # 指定读写权限，可以开始写入数据
        self.csvexporter.start_exporting()

    def process_item(self, item, spider):
        # 将item数据写入到csv文件里
        self.csvexporter.export_item(item)
        return item

    def close_spider(self, spider):
        # 表述数据写入结束
        self.csvexporter.finish_exporting()
        self.csv.close()
