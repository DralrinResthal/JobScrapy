# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobScraperItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    company = scrapy.Field()
    salary = scrapy.Field()
