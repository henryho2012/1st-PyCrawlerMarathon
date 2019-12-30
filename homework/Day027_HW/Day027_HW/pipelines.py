# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json

class Day027HwPipeline(object):
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
    def open_spider(self, spider):
        print('Start!!')
        self.file = open('Day27_HW.txt', 'w')
    def close_spider(self, spider):
        self.file.close()
        print('Finished!!')
