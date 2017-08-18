# -*- coding: utf-8 -*-

# Scrapy settings for text project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'


#COOKIES_ENABLED = True 

#ITEM_PIPELINES = {
#   'text.pipelines.TextPipeline':300
#}

DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'tutorial.rotate_useragent.RotateUserAgentMiddleware' :400
#'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':110,
#       'pythontab.middlewares.ProxyMiddleware':100,

    }


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'text (+http://www.yourdomain.com)'
