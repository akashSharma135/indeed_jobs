import scrapy


class JobProfileCrawlerSpider(scrapy.Spider):
    name = 'job_profile_crawler'
    allowed_domains = ['https://in.indeed.com/jobs']
    start_urls = ['http://https://in.indeed.com/jobs/']

    def parse(self, response):
        pass
