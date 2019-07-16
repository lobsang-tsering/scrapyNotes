import scrapy 

class scrapData(scrapy.Spider):
    
    name = 'data1'
    start_urls = [
           'http://quotes.toscrape.com/'
           ]

    
    
    def parse(self, response):
    
        allData = response.css('div.quote')
        for item in allData : 
            title = item.css('span.text::text').extract()
            author = item.css('.author::text').extract()
            tag = item.css('.tag::text').extract()
            yield {
                    'title' : title,
                    'author' : author,
                    'tag' : tag
            }
