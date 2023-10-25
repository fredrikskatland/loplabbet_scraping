from typing import Iterable
import scrapy
from scrapy.http import Request
from scrapy_playwright.page import PageMethod
from loplabbet.items import LoplabbetItem
from scrapy.loader import ItemLoader
import pandas as pd

class BaseLopeskoSpider(scrapy.Spider):
    def __init__(self, gender, category, *args, **kwargs):
        super(BaseLopeskoSpider, self).__init__(*args, **kwargs)
        self.gender = gender
        self.category = category
        self.start_url = f'https://www.loplabbet.no/kategorier/{self.gender}/lopesko/{self.category}?sortOrder=CreatedDescending&numProducts=1000'
        self.collected_items = []  # Initialize the list to store items

        # Create a filename based on gender and category
        filename = f"{self.gender}_{self.category}.json"
        
        # Update custom settings for this spider
        #self.custom_settings = {
        #    'FEEDS': {
        #        filename: {
        #            'format': 'json',
        #            'encoding': 'utf8',
        #            'store_empty': False,
        #            'fields': None,
        #            'indent': 4,
        #        },
        #    },
        #}

    def start_requests(self):
        yield scrapy.Request(self.start_url,
                             meta=dict(
                                 playwright=True,
                                 playwright_include_page=True,
                                 playwright_page_methods=[
                                     PageMethod('wait_for_selector', 'p.ll-categoryProducts__pagination-statusText')
                                     ]
                             ))

    async def parse(self, response):
        items = []  # list to store all the scraped items
        for products in response.css('a.ll-link-product-card'):
            l = ItemLoader(item=LoplabbetItem(), selector=products)
            l.add_value('links', products.attrib['href'])
            l.add_value('gender', self.gender)
            l.add_value('category', self.category)

            items.append(l.load_item())  # add the item to the list
        
        self.collected_items.extend(items)  # assuming self.collected_items is initialized in __init__

        # Your logic to detect the last page, then send the collected items to pipeline
        yield {'collected_items': self.collected_items}

class DameKonkurranseskoSpider(BaseLopeskoSpider):
    name = 'dame_konkurransesko'
    
    def __init__(self, *args, **kwargs):
        super(DameKonkurranseskoSpider, self).__init__('dame', 'konkurransesko', *args, **kwargs)

class DameTreningsskoSpider(BaseLopeskoSpider):
    name = 'dame_treningssko'
    
    def __init__(self, *args, **kwargs):
        super(DameTreningsskoSpider, self).__init__('dame', 'treningssko', *args, **kwargs)

class DameFritidsskoSpider(BaseLopeskoSpider):
    name = 'dame_fritidssko'
    
    def __init__(self, *args, **kwargs):
        super(DameFritidsskoSpider, self).__init__('dame', 'fritidssko', *args, **kwargs)

class DamePiggskoSpider(BaseLopeskoSpider):
    name = 'dame_piggsko'
    
    def __init__(self, *args, **kwargs):
        super(DamePiggskoSpider, self).__init__('dame', 'piggsko', *args, **kwargs)

class DameTerrengskoSpider(BaseLopeskoSpider):
    name = 'dame_terrengsko'
    
    def __init__(self, *args, **kwargs):
        super(DameTerrengskoSpider, self).__init__('dame', 'terrengsko', *args, **kwargs)

class DameVinterpiggskoSpider(BaseLopeskoSpider):
    name = 'dame_vinterpiggsko'
    
    def __init__(self, *args, **kwargs):
        super(DameVinterpiggskoSpider, self).__init__('dame', 'vinterpiggsko', *args, **kwargs)

class HerreKonkurranseskoSpider(BaseLopeskoSpider):
    name = 'herre_konkurransesko'
    
    def __init__(self, *args, **kwargs):
        super(HerreKonkurranseskoSpider, self).__init__('herre', 'konkurransesko', *args, **kwargs)

class HerreTreningsskoSpider(BaseLopeskoSpider):
    name = 'herre_treningssko'
    
    def __init__(self, *args, **kwargs):
        super(HerreTreningsskoSpider, self).__init__('herre', 'treningssko', *args, **kwargs)

class HerreFritidsskoSpider(BaseLopeskoSpider):
    name = 'herre_fritidssko'
    
    def __init__(self, *args, **kwargs):
        super(HerreFritidsskoSpider, self).__init__('herre', 'fritidssko', *args, **kwargs)

class HerrePiggskoSpider(BaseLopeskoSpider):
    name = 'herre_piggsko'

    def __init__(self, *args, **kwargs):
        super(HerrePiggskoSpider, self).__init__('herre', 'piggsko', *args, **kwargs)

class HerreTerrengskoSpider(BaseLopeskoSpider):
    name = 'herre_terrengsko'
    
    def __init__(self, *args, **kwargs):
        super(HerreTerrengskoSpider, self).__init__('herre', 'terrengsko', *args, **kwargs)

class HerreVinterpiggskoSpider(BaseLopeskoSpider):
    name = 'herre_vinterpiggsko'
    
    def __init__(self, *args, **kwargs):
        super(HerreVinterpiggskoSpider, self).__init__('herre', 'vinterpiggsko', *args, **kwargs)
