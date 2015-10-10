import scrapy
import urllib
from ImageCrawl.items import ImagecrawlItem
import json

class InstagramSpider(scrapy.Spider):
    name = "Instagram"
    tag=''
    page_cnt=3 # return count=page_cnt*20
    params = {
        'access_token': '',
    }
    start_urls = [
        'https://api.instagram.com/v1/tags/'+tag+'/media/recent?'+ urllib.urlencode(params)
    ]

    def parse(self, response):
        response =json.loads(response.body)
        for result in response['data']:
            item = ImagecrawlItem()
            item['host']=self.name
            item['s']=self.tag
            item['src_link']=result['images']['standard_resolution']['url']
            yield item
        next_url= response['pagination']['next_url']
        if self.page_cnt>1:
            self.page_cnt-=1
            yield scrapy.Request(next_url, self.parse)