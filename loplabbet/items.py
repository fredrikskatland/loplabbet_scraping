# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

base_url = 'https://www.loplabbet.no'
def add_base_url(value):
    return base_url + value
    

class LoplabbetItem(scrapy.Item):
    # define the fields for your item here like:
    links = scrapy.Field(input_processor=MapCompose(add_base_url), output_processor=TakeFirst())
    gender = scrapy.Field(output_processor=TakeFirst())
    category = scrapy.Field(output_processor=TakeFirst())
