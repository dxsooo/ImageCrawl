# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import os
import csv

from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem

class ImagecrawlPipeline(object):
    def process_item(self, item, spider):
        return item

class DataWriterPipeline(object):
    writer=None
    def __init__(self):
        if os.path.isdir('csv'):
            pass
        else:
            os.makedirs('csv')
        self.fn=time.strftime('csv/%Y%m%d%H%M%S',time.localtime())+'.csv'

    def process_item(self, item, spider):
        if self.writer==None:
            self.writer = csv.writer(open(self.fn, 'wb'))
        self.writer.writerow([item['host'],item['s'],item['src_link']])
        return item

class ImagesDownloadPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        return '%s' % (image_guid)

    def get_media_requests(self, item, info):
        yield Request(item['src_link'])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item