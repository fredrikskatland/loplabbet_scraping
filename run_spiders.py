from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import time

# Define genders and categories
genders = ['dame', 'herre']
categories = ['konkurransesko', 'treningssko', 'fritidssko', 'piggsko', 'terrengsko', 'vinterpiggsko']

# Initialize CrawlerProcess with your project settings
process = CrawlerProcess(get_project_settings())

# Iterate through combinations
for gender in genders:
    for category in categories:
        # Wait for 3 seconds
        time.sleep(3)
        filename = f"{gender}_{category}.json"
        crawler = f"{gender}_{category}"
        
        # Update feed settings dynamically
        process.settings.set('FEEDS', {
            filename: {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': False,
                'fields': None,
                'indent': 4,
            }
        })
        
        # Start crawling
        process.crawl(crawler)

# Start the CrawlerProcess
process.start()
