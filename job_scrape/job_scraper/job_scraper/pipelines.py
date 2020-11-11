import pymongo
from dotenv import load_dotenv
from os import getenv
from datetime import datetime
from itemadapter import ItemAdapter

load_dotenv()


class JobScraperPipeline:
    def __init__(self):    
        self.client = pymongo.MongoClient(getenv("MONGO_URI"))
        db = self.client['jobList']
        self.collection = db['jobs']
        time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        self.filename = f'{time}_db_logs.log'

    def log_db_entries(self, log_text):
        with open(self.filename, 'a') as f:
            f.write(log_text)

    def process_item(self, item, spider):
        if not self.collection.count_documents({'title':item['title'],'company':item['company']}, limit=1) !=0:
            log_text = f'Job not found: {item["title"]}\nURL: {item["link"]}\nInserting job to database.\n'
            print(log_text)
            self.log_db_entries(log_text)
            self.collection.insert(dict(item))
        else:
            log_text = f'Job found: {item["title"]}\nMoving to next item...\n'
            print(log_text)
            self.log_db_entries(log_text)
