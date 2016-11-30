# -*- coding: utf-8 -*-
import scrapy
import datetime, time
import httplib, urllib
from scrapy.crawler import CrawlerProcess

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class MyCrawler(scrapy.Spider):
    name = 'NAVER_STANDARD_CRAWLER'
    start_urls = ['']


    #    /PostView.nhn?blogId=rlaalsckd11&logNo=220818063856&redirect=Dlog&widgetTypeCall=true
    real_id= start_urls[0][22:-13] # blog id
    real_num=start_urls[0][-12:] # log No




    real_url= ['http://blog.naver.com/PostView.nhn?blogId='+real_id+'&logNo='+real_num+'&redirect=Dlog&widgetTypeCall=true']

    start_urls = real_url

    def to_id(self, value):
        hour, minute = value.split(':')
        today = datetime.datetime.today()
        today.replace(hour=int(hour), minute=int(minute), microsecond=0)
        return str(time.mktime(today.timetuple()))

    def parse(self, response):

        # text = response.css("iframe::attr(src)")
        # text = response.css("frame::attr(src)")
        img = response.css("img::attr(src)").extract()
        text = response.css("div p span::text").extract()

        print "Naver Crawler"

        for i in img:
            print i
        for j in text:
            print j



process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MyCrawler)
process.start()
