# ImageCrawl

## Overview
Based on [Scrapy](https://github.com/scrapy/scrapy), ImageCrawl is a web image crawler for websites.   
Recently supports:  

* [Flickr](https://www.flickr.com/)  
* [Instagram](https://instagram.com/)

## Requirements  
* Python 2.7
* [Scrapy](http://scrapy.org/)
* GoAgent (if you are working in China mainland and disconnecting with the target website )

## Documentation
You can go to the top level directory of this project and run:  

    scrapy crawl [spider name]

In this project, the spider name can be `Flickr`, `Instagram`(no buckets). But you need to edit the file `spiders/xxx_spider.py` before you run the command above.  

For ***Flickr***, you should have your own `api_key` (see [here](https://www.flickr.com/services/apps/create/apply/)), and decide your search tag. If you want to change other params, look at the file carefully or get help from [Flickr API](https://www.flickr.com/services/api/). 

    class FlickrSpider(scrapy.Spider):
        name = "Flickr"
        tag='your tag'
        api_key='your api_key'


For ***Instagram***, you should have your own `access_token` (see [here](http://jelled.com/instagram/access-token)), and decide your search tag. If you want to change other params, look at the file carefully or get help from [Instagram API](https://instagram.com/developer/). 

    class InstagramSpider(scrapy.Spider):
        name = "Instagram"
        tag='your tag'
        params = {
        	'access_token': 'your access_token',
    	}

You will get a `csv` folder that stores the crawl result(named with the beginning time of the program) and the images downloaded to folder `data` when the program finished.  
If you want to change the image download directory, edit the last line in file `settings.py`.  

    IMAGES_STORE = 'data'
	
**Note** the program works with GoAgent by default, please ensure your GoAgent works well and pre-opened, change or disable GoAgent, see [this](http://snipplr.com/view/74665/using-goagent-agent-in-scrapy/).