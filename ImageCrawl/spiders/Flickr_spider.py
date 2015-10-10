import scrapy
import urllib
from ImageCrawl.items import ImagecrawlItem

class FlickrSpider(scrapy.Spider):
    name = "Flickr"
    tag=''
    api_key=''
    params = {
        'method':'flickr.photos.search',
        'api_key': api_key,
        'sort':'relevance', #sort by relevance
        'per_page':10, #per-page return 10 picture,max=500
        'tags':tag
    }

    params2 = {
        'api_key': api_key,
        'method':'flickr.photos.getSizes',
        'photo_id':''
    }
    start_urls = [
        'https://api.flickr.com/services/rest/?'+ urllib.urlencode(params)
    ]

    def parse(self, response):
        for pid in response.xpath('//photo/@id'):
            self.params2['photo_id']=pid.extract()
            url='https://api.flickr.com/services/rest/?'+ urllib.urlencode(self.params2)
            yield scrapy.Request(url,callback=self.parse_biggest)

    def parse_biggest(self, response):
        item = ImagecrawlItem()
        item['host']=self.name
        item['s']=self.tag
        item['src_link']=response.xpath('//size/@source')[-1].extract() #return the largest image if the image has multi sizes
        return item