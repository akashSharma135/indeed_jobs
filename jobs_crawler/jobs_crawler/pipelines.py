# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class JobsCrawlerPipeline:
    def __init__(self) -> None:
        self.conn = pymongo.MongoClient("mongodb+srv://akash:8jNYW8eVQCHORH6M@cluster0.k8zrx.mongodb.net/jobsDB?retryWrites=true&w=majority")

        db = self.conn['jobsDB']
        self.collection = db['jobs']

    def process_item(self, item, spider):
        self.collection.insert_one({
            'title': item['title'],
            'company': item['company'],
            'address': item['address'],
            'type': item['type'],
            'salary': item['salary'],
            'description': item['description']
        })
        return item
