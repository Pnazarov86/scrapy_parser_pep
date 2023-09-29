import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """Парсинг PEP."""
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        """Метод собирает ссылки на документы PEP."""
        peps_list = response.css(
            ('section#numerical-index tr a::attr(href)')
        )
        for pep in peps_list:
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        """Метод парсит информацию о PEP."""
        data = {
            'number': response.css('h1.page-title::text').get().split(' ')[1],
            'name': ''.join(
                response.css('h1.page-title::text').get()
            ).strip(),
            'status': response.css('abbr::text').get(),
        }
        yield PepParseItem(data)
