# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TanqinbaItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    des = scrapy.Field()
    singer = scrapy.Field()
    seeNum = scrapy.Field()
    collectNum = scrapy.Field()
    hard = scrapy.Field()
    user = scrapy.Field()
    time = scrapy.Field()
    commentUser = scrapy.Field()
    commentDate = scrapy.Field()
    commentContent = scrapy.Field()
    pass
