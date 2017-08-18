# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field


class JohnsItem(Item):
    text = Field()

# name = Field()
#   URL = Field()
#   price = Field()

