import scrapy

class JobsCrawlerItem(scrapy.Item):
    profile = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    salary = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
