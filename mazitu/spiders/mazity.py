import scrapy

from mazitu.items import MazituItem

class MazituSpider(scrapy.Spider):
    name = "mazitu"
    start_url=['https://www.mzitu.com/xinggan/']

    