try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.selector import Selector
from scrapy.item import Item 
import sys
sys.path.append('/home/zhangpeng/github/Crawler/scrapy1.0/tutorial/tutorial')
from items import *
from scrapy.http import Request
class johnsSpider(Spider):
    download_delay = 0 
    name = 'johns'
    allowed_domains = ["list.tmall.com"]
    start_urls = ['http://list.tmall.com/search_product.htm?spm=141.3067357.%20%20%20%201.1.jzZAw2&cat=50918004&acm=lb-tms-974440-56585.1003.4.176540%20%20%20%20&scm=1003.4.lb-%20%20%20%20tms-974440-56585.OTHER_1_176540']

    def parse(self, response):
        hxs = Selector(response)
#       site_price = hxs.xpath('//em[@title]')
# passed = hxs.xpath('//div[@class = "product"]')
#  for i in range(len(site_price)): 
# a = hxs.xpath('//div/div/b')
#       b = a.xpath('.//a')[len(b.xpath('.//a'))-1]
#       c = 'http://list.tmall.com/search_product.htm'+c.xpath('@href').extract()[0]
        page = hxs.xpath('//div/div/b/b[@class= "ui-page-cur"]/text()').extract()[0]
        if int(page) <=17:
            b = int(page)*60
            c ='http://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.3ABSsN&cat=50918004&s='+str(b)+'&sort=s&style=g&active=1&industryCatId=50918004&type=pc#J_Filter'
            yield scrapy.Request(c,callback= self.parse)
        item = JohnsItem()
        item['text'] = c
        yield item
# site_name = passed[i].select('.//a[@href][@title][@data-p]')[0]
#           item['price'] = site_price[i].select('text()').extract()[0]
#           item['name']=site_name.select('text()').extract()
#           item['URL']='http:'+site_name.select('@href').extract()[0]
'''scrapy crawl johns -o item.json -t json'''
