import pymongo

class JobsCrawlerPipeline:
    def __init__(self) -> None:
        self.conn = pymongo.MongoClient("mongodb+srv://akash:8jNYW8eVQCHORH6M@cluster0.k8zrx.mongodb.net/jobsDB?retryWrites=true&w=majority")

        db = self.conn['jobsDB']
        self.collection = db['jobs']

    def process_item(self, item, spider):
        self.collection.insert_one({
            'profile': item['profile'],
            'company': item['company'],
            'location': item['location'],
            'salary': item['salary'],
            'description': item['description'],
            'url': item['url']
        })
        return item
