import scrapy
from scrapy.linkextractors import LinkExtractor
from .models import Links, Category
import os

class Scraper(scrapy.Spider):
    name = "test"

    def __init__(self, *args, **kwargs):
        self.start_urls = kwargs.pop('url', [])
        self.basename = os.path.basename(self.start_urls[0])
        self.user_id = kwargs.pop('user_id')
        super(Scraper, *args, **kwargs)
    
    def save_category(self, total_links):
        c = Category()
        c.name = self.basename
        c.total_links = total_links
        c.user_id = self.user_id
        c.save()
        return c.id
    
    def save_link(self, object):
        l = Links()
        l.name = object["text"]
        l.link = object["url"]
        l.category_id = object["category_id"]
        l.save()

    def parse(self, response):
        link_ext = LinkExtractor()
        links = link_ext.extract_links(response)
        cat_id = self.save_category(len(links))
        for link in links:
            tmp = {}
            tmp["url"] = link.url
            tmp["text"] = link.text
            tmp["category_id"] = cat_id
            self.save_link(tmp)
            yield tmp
