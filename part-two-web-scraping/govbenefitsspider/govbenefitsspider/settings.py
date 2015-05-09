# -*- coding: utf-8 -*-

# Scrapy settings for govbenefitsspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'govbenefitsspider'

SPIDER_MODULES = ['govbenefitsspider.spiders']
NEWSPIDER_MODULE = 'govbenefitsspider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'govbenefitsspider (+http://www.yourdomain.com)'

# Be nice to the sites we're crawling
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5.0
AUTOTHROTTLE_MAX_DELAY = 60.0
DOWNLOAD_DELAY = 5

# Disable cookies
COOKIES_ENABLED = False

# Use the fake_useragent python library
# Requires you to: pip install fake-useragent
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'govbenefitsspider.middlewares.RandomUserAgentMiddleware': 400,
}


