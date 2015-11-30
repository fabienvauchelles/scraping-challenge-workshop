# -*- coding: utf-8 -*-

BOT_NAME = 'myscraper'

SPIDER_MODULES = ['myscraper.spiders']
NEWSPIDER_MODULE = 'myscraper.spiders'

CONCURRENT_REQUESTS_PER_DOMAIN = 1
RETRY_TIMES = 0

# PROXY
PROXY = 'http://127.0.0.1:8888/?noconnect'

# SCRAPOXY
API_SCRAPOXY = 'http://127.0.0.1:8889/api'
API_SCRAPOXY_PASSWORD = 'CHANGE_THIS_PASSWORD'

# BLACKLISTING
BLACKLIST_HTTP_STATUS_CODES = # TO FILL

DOWNLOADER_MIDDLEWARES = {
    'scrapoxy.downloadmiddlewares.proxy.ProxyMiddleware': 100,
    'scrapoxy.downloadmiddlewares.wait.WaitMiddleware': 101,
    'scrapoxy.downloadmiddlewares.scale.ScaleMiddleware': 102,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    # TO FILL (use the BlacklistDownloaderMiddleware from Scrapoxy SDK)
}
