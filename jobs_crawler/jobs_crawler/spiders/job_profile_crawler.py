import scrapy
import re
from bs4 import BeautifulSoup
import requests

class JobProfileCrawlerSpider(scrapy.Spider):
    name = 'job_profile_crawler'
    allowed_domains = ['indeed.com']

    profile = input("profile: ")
    location = input("location: ")

    start_urls = [f'https://in.indeed.com/jobs?q={profile}&l={location}']

    # get proxy list
    def __init__(self):
        URL = 'https://free-proxy-list.net/'

        res = requests.get(URL)

        soup = BeautifulSoup(res.content, 'html.parser')

        proxies_list = []
        for trs in soup.find('div', 'table-responsive').find('tbody').find_all('tr'):
            tds = trs.find_all('td')

            ip = tds[0].text
            port = tds[1].text

            proxies_list.append(ip + ":" + port)

        with open('jobs_crawler/proxies.txt', 'w') as file:
            for data in proxies_list:
                file.writelines(f"{data}\n")


    def parse(self, response):

        # getting the url of detailed page
        for href in response.css('.tapItem::attr(href)'):
            url = response.urljoin(href.extract())
            # making a request for detail page and calling method parse_items to get data
            yield scrapy.Request(url, callback=self.parse_items)
            
        # getting url for next page
        next_page_href = response.css('.pagination-list > li:last-child > a::attr(href)')
        next_page_url = response.urljoin(next_page_href.get())
        # making request for next page
        yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_items(self, response):
        for selector in response.xpath('//*[@id="viewJobSSRRoot"]/div/div[1]/div[3]/div/div/div[1]/div[1]'):

            content = ""
            description = str(selector.css('#jobDescriptionText').get())
            if description is not None:
                content = re.sub('<.*?>', '', description)

            url = response.url
            container = selector.css('.jobsearch-DesktopStickyContainer')
            profile = container.css('.jobsearch-JobInfoHeader-title-container h1::text').get()
            company = container.css('.icl-u-lg-mr--sm::text').get()
            if company is None:
                company = container.css('.icl-u-xs-mr--xs a::text').get()
            salary = container.css('.jobsearch-JobMetadataHeader-item > .icl-u-xs-mr--xs::text').get()
            
            yield {
                "profile": profile if profile else "",
                "company": company if company else "",
                "salary": salary if salary else "",
                "location": JobProfileCrawlerSpider.location,
                "description": content if content else "",
                "url": url
            }
