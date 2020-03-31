import scrapy


class AmzcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    item_name = scrapy.Field()
    item_creator = scrapy.Field()
    item_price = scrapy.Field()
    #name = scrapy.Field()
    pass
