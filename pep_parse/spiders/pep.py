import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """Парсинг PEP."""
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        peps_list = response.css(
            ('section#numerical-index tr a::attr(href)')
        )
        for pep in peps_list:
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': response.css('h1.page-title::text').get(),
            'name': ' '.join(
                response.css('h1.page-title::text').get().split()
            ),
            'status': response.css('abbr::text').get(),
        }
        yield PepParseItem(data)