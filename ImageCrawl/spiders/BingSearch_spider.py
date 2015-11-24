import scrapy
import urllib
from ImageCrawl.items import ImagecrawlItem
import json

class BingSearchSpider(scrapy.Spider):
    name = "BingSearch"
    key_word='your key_word'
    acctKey = 'your account key'

    page_cnt=3

    params = {
            '$format': 'json',
            'Query': '\''+key_word+'\'',
            '$top': 10,
            '$skip': 0
    }

    start_urls = []
    for i in xrange(0,page_cnt):
        start_urls.append('https://api.datamarket.azure.com/Bing/Search/Image?'+ urllib.urlencode(params))
        params['$skip']+=params['$top']

    http_pass=acctKey

    def parse(self, response):
        response =json.loads(response.body)
        for result in response['d']['results']:
            item = ImagecrawlItem()
            item['host']=self.name
            item['s']=self.key_word
            item['src_link']=result['MediaUrl']
            yield item