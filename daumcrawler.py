# -*- coding: utf-8 -*-
import scrapy
import datetime, time
from scrapy.crawler import CrawlerProcess

import sys

reload(sys)
sys.setdefaultencoding('utf-8')



class MyCrawler(scrapy.Spider):
    name = 'daumcrawler'

   //after doing frame, iframe
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
        text1 = response.css("#contentDiv img::attr(src)").extract()
        text2 = response.css("#contentDiv > p span::text").extract()

        for i in text1 :
            print i
        for j in text2 :
            print j

       

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MyCrawler)
process.start()
