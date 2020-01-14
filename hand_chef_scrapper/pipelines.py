# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.utils.project import get_project_settings
import logging
settings = get_project_settings()


class HandChefScrapperPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        # Drop invalid data
        for data in item:
            if not data:
                raise DropItem("Missing data!")

        self.collection.update({'url': item['url']}, dict(item), upsert=True)
        logging.log(logging.INFO ,'Recipe added!')
        return item
