from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

import re


class JobProfileCrawlerSpider(CrawlSpider):
    name = 'job_profile_crawler'
    allowed_domains = ['indeed.com']
    profile = input("enter profile: ")
    location = input("enter location: ")

    start_urls = [f'https://in.indeed.com/jobs?q={profile}&l={location}']

    job_detail_le = Rule(LinkExtractor(restrict_css='.tapItem'), follow=False, callback='parse_item')

    next_page_le = Rule(LinkExtractor(restrict_xpaths='#resultsCol > nav > div > ul > li:nth-child(6) > a::href'), follow=True)

    rules = (
        job_detail_le,
        next_page_le
    )

    def parse_item(self, response):

        data = response.css('#jobDescriptionText').get()
        content = ""
        if data is not None:
            content = re.sub('<.*?>', '', data)

        
        yield {
            'title': response.css('.jobsearch-JobInfoHeader-title::text').get(),
            'company': response.css('.icl-u-lg-mr--sm::text').get(),
            'address': response.css('.jobsearch-DesktopStickyContainer-companyrating+ div::text').get(),
            'type': response.css('.jobsearch-DesktopStickyContainer-companyrating~ div+ div::text').get(),
            'salary': response.css('.jobsearch-JobMetadataHeader-item .icl-u-xs-mr--xs::text').get(),
            'description': content
        }
