import scrapy

class Recipe(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    thumb = scrapy.Field()
    ingredients = scrapy.Field()
    directions = scrapy.Field()
    readyInTime = scrapy.Field()
    servings = scrapy.Field()
