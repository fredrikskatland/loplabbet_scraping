# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from loplabbet.update_index import update_index
import pandas as pd

class LoplabbetPipeline:
    def process_item(self, item, spider):
        df = pd.DataFrame(item['collected_items'])
        print(df.head())
        update_index(df, indexing_type="incremental")
        return item
