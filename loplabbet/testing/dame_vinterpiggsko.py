from typing import Iterable
import scrapy
from scrapy.http import Request
from scrapy_playwright.page import PageMethod


class LopeskoSpider(scrapy.Spider):
    name = "dame_vinterpiggsko"

    def start_requests(self):
        yield scrapy.Request('https://www.loplabbet.no/kategorier/dame/lopesko/vinterpiggsko?sortOrder=CreatedDescending&numProducts=1000'
                             , meta=dict(
                                 playwright=True,
                                 playwright_include_page=True,
                                 playwright_page_methods=[
                                     PageMethod('wait_for_selector', 'p.ll-categoryProducts__pagination-statusText')
                                     ]
                             ))

    async def parse(self, response):
        for products in response.css('a.ll-link-product-card'):
            yield {
                'links': 'https://www.loplabbet.no'+products.attrib['href'],
                'kjonn': 'dame',
                'kategori': 'vinterpiggsko'
            }