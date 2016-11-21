# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name=u'scrapers',
    version=u'1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points = {'scrapy': ['settings = myscraper.settings']}
)

