import scrapy

from pep_parse.items import PepParseItem
from pep_parse.utils import get_pep_name_number


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{url}/' for url in allowed_domains]

    def parse(self, response):
        index_by_category = response.xpath(
            '//section[@id="index-by-category"]'
        )
        pep_links = index_by_category.css('tr a::attr(href)').getall()
        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        text_title = response.xpath('//h1[@class="page-title"]/text()').get()
        number, name = get_pep_name_number(self, text_title)
        status = response.xpath('//abbr/text()').get()
        data = {
            'number': number,
            'name': name,
            'status': status
        }
        yield PepParseItem(data)
