import re
import scrapy

from mazitu.items import MazituItem

class MazituSpider(scrapy.Spider):
    name = "mazitu"
    start_urls =['https://www.mzitu.com']
    # for i in range(1,141):
    #     url = "https://www.mzitu.com/xinggan/page/{}/".format(i)
    #     start_urls.append(url)

    def parse(self, response):
        for pin in response.xpath("//*[@id='pins']/li/a"):
           url  = pin.attrib["href"]
           yield scrapy.Request(url,callback=self.parse_page)
        next_page = response.xpath("//*[@class='next page-numbers']")[0].attrib["href"]
        yield scrapy.Request(next_page,callback=self.parse)

    def parse_page(self,response):
        img = response.xpath("//*[@class='main-image']/p/a/img").attrib["src"]
        print(img)
        next_page_text = response.xpath("//*[@class='pagenavi']/a[last()]").extract()
        if "下一页" in next_page_text:
            next_page = response.xpath("//*[@class='pagenavi']/a[last()]")[0].attrib["href"]
            yield scrapy.Request(next_page,callback=self.parse_page)

        
