# -*- coding: utf-8 -*-

from scrapy import Spider, Request
from ..items import PersonItem


class MyScraper(Spider):
    name = u'myscraper'


    def start_requests(self):
        # Use a loop (for i in range(0, 1))
        for i in range(0, 50):
            yield Request(
                url='https://scraping-challenge.herokuapp.com/pagination?page=%d' % i,
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
