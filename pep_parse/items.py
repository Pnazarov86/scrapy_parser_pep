import scrapy


class PepParseItem(scrapy.Item):
    """Хранение результатов парсинга."""
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
