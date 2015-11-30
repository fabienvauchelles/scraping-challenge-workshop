# -*- coding: utf-8 -*-

from scrapy import Spider, Request, FormRequest
from ..items import PersonItem


class MyScraper(Spider):
    name = u'myscraper'


    def start_requests(self):
        # 1/ Use a FormRequest instead of a Request
        # 2/ Pass email and password with formdata
        # 3/ Find the good URL to post data !
        yield Request(
            url=u'https://scraping-challenge.herokuapp.com/login',
            callback=self.parse,
        )


    def parse(self, response):
        # Find a list of div which contains a person (use CSS)
        persons_el = response.css('.person')

        # Browse the list
        for person_el in persons_el:

            # Create a new item
            item = PersonItem()

            # Extract the name of the person (use CSS)
            item['name'] = person_el.css('.name::text').extract_first()

            # Extract the ticket fare of the person (use CSS)
            item['ticket_fare'] = person_el.css('.ticket_fare::text').extract_first()

            # Export the item
            yield item


