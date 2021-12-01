# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsCrawlerItem(scrapy.Item):
    title = scrapy.Field()
    company = scrapy.Field()
    address = scrapy.Field()
    type = scrapy.Field()
    salary = scrapy.Field()
    description = scrapy.Field()
