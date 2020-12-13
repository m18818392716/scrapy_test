# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderobjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tag = scrapy.Field()  # 标签字段
    content = scrapy.Field()  # 名言内容
    pass

class CityItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 城市名称
    url = scrapy.Field()  # 城市对应url
    pass

class QunarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DetailItem(scrapy.Item):
    # 抓取内容：1.帖子标题；2.帖子作者；3.帖子回复数
    title = scrapy.Field()
    author = scrapy.Field()
    reply = scrapy.Field()

class NewsItem(scrapy.Item):
    # 抓取内容：1.帖子标题；2.帖子作者；3.帖子回复数
    title = scrapy.Field()
    imgsrc = scrapy.Field()
    # source = scrapy.Field()
