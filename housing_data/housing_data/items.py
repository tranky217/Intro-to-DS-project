# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HousingDataItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field() 
    price = scrapy.Field()
    acreage = scrapy.Field()
    street = scrapy.Field()
    district = scrapy.Field()
    city = scrapy.Field()
    type = scrapy.Field()
    legal_status = scrapy.Field()
    corner_unit = scrapy.Field()
    num_of_bedrooms = scrapy.Field()
    num_of_floors = scrapy.Field()
    interior = scrapy.Field()
    area_population = scrapy.Field()
    area_acreage = scrapy.Field()
    being_sold_properties = scrapy.Field()
    balcony_direction = scrapy.Field()
    house_direction = scrapy.Field()
    facade = scrapy.Field()
    way_in = scrapy.Field()
    # pass
