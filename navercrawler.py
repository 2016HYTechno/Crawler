# -*- coding: utf-8 -*-
import scrapy
import itertools
from scrapy.crawler import CrawlerProcess


class MyCrawler(scrapy.Spider):
    name = 'NAVER_STANDARD_CRAWLER'
    start_urls = ['http://blog.naver.com/o0owldus/220865244803']
    #http://blog.naver.com/hypoid613/220792561480
    #http://blog.naver.com/rlaalsckd11/220818063856
    #http://blog.naver.com/qjarl111/220819887238
    #http://blog.naver.com/pahiri/220825087621
    #http://blog.naver.com/lol_llo/220825994541


    #    /PostView.nhn?blogId=rlaalsckd11&logNo=220818063856&redirect=Dlog&widgetTypeCall=true
    real_id= start_urls[0][22:-13] # blog id
    real_num=start_urls[0][-12:] # log No


    text4 = "#post-view"+real_num+ "> div ::attr(id)"

    real_url= ['http://blog.naver.com/PostView.nhn?blogId='+real_id+'&logNo='+real_num+'&redirect=Dlog&widgetTypeCall=true']

    start_urls = real_url
    print real_url[0]
    def parse(self, response):

        # text1 = response.css("div#post-view220800717202 > div img::attr(src)").extract()
        # original_url = response.css("frame::attr(src)").extract()
        # print original_url
        #text1 = response.css("#SEDOC-1474515978302-1648338688 > div p span::text").extract()



        #print self.text4
        text3 = response.css(self.text4).extract()  # id of body
        print text3[0]
        #print text3[0]
        #text = response.css("#"+text3[0]+"> div p span::text").extract()
        text = response.css("#" + text3[0] + "> div p span").extract()
        img = response.css("#"+text3[0]+"> div img::attr(src)").extract()
        for i in img:
            print i

        text6 = response.css("#"+text3[0]+" > div.se_component_wrap.sect_dsc.__se_component_area > div > div > div > div > div >  div ::text").extract()

        #for j in range(1,37,2):
            #text7 = response.css("#SEDOC-1474515978302-1648338688 > div.se_component_wrap.sect_dsc.__se_component_area > div:nth-child(j) > div > div > div > div > div > p > span::text").extract()
            #for i in text7:
            #    print i



            # SEDOC-1474515978302-1648338688 > div.se_component_wrap.sect_dsc.__se_component_area > div:nth-child(37) > div > div > div > div > div
        #    print i

        #for i in text:
        #    print i
        #for i,j in zip (img,text6):
        #    print i
        #for i in img:
        #    print i
        a=1
        while a:
            for i in text6:
                if i == '\n' + '                    ':
                    print img[a]
                    a=a+1
                else:
                    print i
            break



process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MyCrawler)
process.start()