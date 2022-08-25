import scrapy

f = open('input.txt', 'r', encoding='utf-8')

product = f.read().strip()

class search_spider_flipkart(scrapy.Spider):
    name = "fkt"

    start_urls = [
        f'https://www.flipkart.com/search?q={product}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as'
        '=off '
    ]

    def parse(self, response):
        results = response.xpath("//div[@class='_4rR01T']/text()").extract()
        price = response.xpath("//div[@class='_30jeq3 _1_WHN1']/text()").extract()
        yield {
            'Name': results,
            'Price': price
        }


class search_spider_amazon(scrapy.Spider):
    name = "amz"

    start_urls = [
        f'https://www.amazon.in/s?k={product}&ref=nb_sb_noss_2'
    ]

    def parse(self, response):
        results = response.xpath("//span[@class ='a-size-medium a-color-base a-text-normal']/text()").extract()
        price = response.xpath("//span[@class = 'a-offscreen']/text()").extract()
        yield {
            'Name': results,
            'Price': price
        }


class search_spider_rd(scrapy.Spider):
    name = 'rd'

    start_urls = [
        f"https://www.reliancedigital.in/search?q={product}:relevance"
    ]

    def parse(self, response):
        results = response.xpath("//p[@class ='sp__name']/text()").extract()
        price = response.xpath("//span[@class = 'sc-bxivhb dmBTBc']/text()").extract()
        yield {
            'Name': results,
            'Price': price
        }