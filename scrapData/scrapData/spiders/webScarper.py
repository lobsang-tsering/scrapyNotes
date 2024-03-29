import scrapy 
from ..items import ScrapdataItem


class scrapData(scrapy.Spider):
    
    name = 'data1'
    start_urls = [
           'http://quotes.toscrape.com/'
           ]

    def parse(self, response):
    
        items  = ScrapdataItem()

        allData = response.css('div.quote')
        for item in allData : 
            title = item.css('span.text::text').extract()
            author = item.css('.author::text').extract()
            tag = item.css('.tag::text').extract()

            items['title'] = title 
            items['author'] = author
            items['tag'] = tag

            yield items
            # yield {
            #         'title' : title,
            #         'author' : author,
            #         'tag' : tag
            # }
