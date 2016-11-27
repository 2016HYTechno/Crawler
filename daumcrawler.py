# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess


class MyCrawler(scrapy.Spider):
    name = 'daumcrawler'

    #start_urls = ['http://blog.daum.net/ktg0205/954']
    #start_urls = ['http://blog.daum.net/ktg0205/954/_blog/BlogTypeView.do?blogid=0eq3B&arti']
    #start_urls = ['http://blog.daum.net/_blog/BlogTypeView.do?blogid=0eq3B&articleno=954&admin=']
    #start_urls = ['http://blog.daum.net/_blog/hdn/ArticleContentsView.do?blogid=0eq3B&articleno=954&looping=0&longOpen=']


    #start_urls = ['http://blog.daum.net/mi_chan1027/943']
    #start_urls = ['http://blog.daum.net/mi_chan1027/943/_blog/BlogTypeView.do?blogid=0mS8T&arti']
    #start_urls = ['http://blog.daum.net/_blog/BlogTypeView.do?blogid=0mS8T&articleno=943&admin=']
    start_urls = ['http://blog.daum.net/_blog/hdn/ArticleContentsView.do?blogid=0mS8T&articleno=943&looping=0&longOpen=']

    #start_urls = ['http://blog.daum.net/tjrrr0304/15932']
    #start_urls = ['http://blog.daum.net/_blog/BlogTypeView.do?blogid=0WFoG&articleno=15932&admin=']
    #start_urls = ['http://blog.daum.net/_blog/hdn/ArticleContentsView.do?blogid=0WFoG&articleno=15932&looping=0&longOpen=']


    #/_blog/hdn/ArticleContentsView.do?blogid

    def parse(self, response):


        #text = response.css("iframe::attr(src)")
        #text = response.css("frame::attr(src)")
        text1 = response.css("#contentDiv img::attr(src)").extract()
        text2 = response.css("#contentDiv > p span::text").extract()

        for i in text1 :
            print i
        for j in text2 :
            print j

        #print text
        #text = response.css("#contentDiv > p> span::text").extract()
        #text = response.css("#contentDiv > p > span >  strong > span > span > span > span > span > span > span::text").extract()
        #text2 = response.css("#contentDiv > p> span > font > strong > span::text").extract()
        #text3 = response.css("#contentDiv > p> span > font > strong > span > span::text").extract()
        #text4 = response.css("#contentDiv > p > span > strong > span::text").extract()
        #text5 = response.css("#contentDiv > p > span > font > strong > span > span").extract()
        #text6 = response.css("#contentDiv > p > span > strong > span").extract()


        #for j in text2 :
         #   print j
        #for k in text3 :
         #   print k

        #for a in text5 :
         #   print a
        #for b in text6 :
         #   print b


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MyCrawler)
process.start()