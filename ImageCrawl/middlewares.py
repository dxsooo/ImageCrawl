from ImageCrawl.settings import USER_AGENT
 
class ImageCrawlMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = USER_AGENT