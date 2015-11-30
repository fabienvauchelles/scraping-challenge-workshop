# -*- coding: utf-8 -*-

from scrapy import Item, Field


class PersonItem(Item):

	url = Field()

	name = Field()
	ticket_fare = Field()
