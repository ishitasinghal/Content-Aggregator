# -*- coding: utf-8 -*-
import scrapy

# class ExampleSpider(scrapy.Spider):
#     name = 'quotes_spider'
#     allowed_domains = ['quotes.toscrape.com']
#     start_urls = ['http://quotes.toscrape.com/']
#
#     def parse(self, response):
#         quotes = response.xpath("//div[@class='quote']//span[@class='text']/text()").extract()
#         author = response.xpath("//div[@class='quote']//small[@class='author']/text()").extract()
#
#         print("Type is: ", type(quotes))
#         print("Type is:", type(author))
#
#         yield  {'quotes': quotes,
#                 'author': author}

class ExampleSpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = ['arstechnica.com']
    start_urls = ['https://arstechnica.com/gaming/2019/08/ewan-mcgregor-confirms-he-will-return-as-obi-wan-for-new-star-wars-series/']

    def parse(self, response):
        print(response)
        quotes = response.xpath("//div[@class='caption-text']//a/@href").extract()

        print(quotes)

        yield  {'quotes': quotes}


from scrapy import cmdline
cmdline.execute("scrapy crawl quotes_spider".split())
