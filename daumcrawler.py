# -*- coding: utf-8 -*-
import scrapy
import datetime, time
import httplib, urllib
from scrapy.crawler import CrawlerProcess

import sys

reload(sys)
sys.setdefaultencoding('utf-8')



class MyCrawler(scrapy.Spider):
    name = 'daumcrawler'

    start_urls = ['']


    #/_blog/hdn/ArticleContentsView.do?blogid

    def to_id(self, value):
        hour, minute = value.split(':')
        today = datetime.datetime.today()
        today.replace(hour=int(hour), minute=int(minute), microsecond=0)
        return str(time.mktime(today.timetuple()))



    def parse(self, response):


        #text = response.css("iframe::attr(src)")
        #text = response.css("frame::attr(src)")
        img = response.css("#contentDiv img::attr(src)").extract()
        text = response.css("#contentDiv > p span::text").extract()

        print "Daum Crawler"

        for i in img :
            print i
        for j in text :
            print j



process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MyCrawler)
process.start()
