# Indeed Job profile scraper

## Summary:

It is a scraper which crawls through all the indeed pages to scrape the content of the available jobs as per the profile and location specified.

## Packages Used:

1. Scrapy
2. scrapy-rotating-proxies
3. scrapy-user-agents
4. BeautifulSoup
5. pymongo["srv"]

## Initial Project Setup:

```bash
git clone https://github.com/akashSharma135/indeed_jobs.git

cd indeed_jobs

python3 -m venv env

source env/bin/activate  (for linux)

env/Scripts/activate (for windows)

git checkout dev-2

pip install -r requirements.txt

cd jobs_crawler

scrapy crawl job_profile_crawler  (add "-o {{filename}}.json" to add data in json file)
```

## Description:

* **__init__(self) method:** is to get the list of free proxies from https://free-proxy-list.net/

* **parse(self, response) method:** requests for the job_profiles page and gets the detail page url of all the profiles and gets the next page url.

* **parse_items(self, response) method:** scrapes the content from the detail page.

## Note:

If database storage is not a need then in settings.py ITEM_PIPELINES can be commented.
