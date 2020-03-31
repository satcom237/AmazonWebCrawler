import scrapy
from ..items import AmzcrawlerItem

class Item:
  def __init__(self, name, price):
    self.name = name
    self.price = price

def findMin(imin, list):
    for i in range(len(list)):
        if list[i].price < imin:
            imin = list[i].price
    #print('--------------', imin)
    return imin

class AmzCrawlerSpider(scrapy.Spider):
    name = 'amz_crawler'
    start_urls = ['https://www.amazon.com/Books/s?srs=17143709011&rh=n%3A283155']

    def parse(self, response):
        items = AmzcrawlerItem()

        item_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        item_price = response.css('.a-spacing-top-small .a-price-whole').css('::text').extract()

        items['item_name'] = item_name
        items['item_price'] = item_price

        #yield items

        items_length = len(items['item_name'])
        # ---Testing---
        #print('--------------', items_length)
        #for i in range(items_length):
            #print(items['item_name'][i])
            
        #prices_length = len(items['item_price'])
        #print('--------------', prices_length)
        #for i in range(prices_length):
            #print(items['item_price'][i])

        list = []
        # ---Testing---
        #list.append(Item(items['item_name'][0], items['item_price'][0])) 
        #print('--------------', list[0].name, list[0].price)
        #list[0].name = items['item_name'][0] # Doesn't work

        j = 0 # variable for price
        for i in range(items_length):
            list.append(Item(items['item_name'][i], int(items['item_price'][j]))) # Cast price from string to int
            j += 2
            print('--------------', list[i].name, list[i].price)

        imin = list[0].price
        imin = findMin(imin, list)

        print('-------Lowest Priced Item/s-------')
        for i in range(len(list)):
            if list[i].price == imin:
                print('>>>>>>>>>>>>>>', list[i].name)


        