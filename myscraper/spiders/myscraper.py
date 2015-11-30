# -*- coding: utf-8 -*-

from scrapy import Spider, Request
from ..items import PersonItem


class MyScraper(Spider):
    name = u'myscraper'


    def start_requests(self):
        # First request
        yield Request(
            url=u'FILL_WITH_URL',
            callback=self.parse,
        )


    def parse(self, response):
        pass
