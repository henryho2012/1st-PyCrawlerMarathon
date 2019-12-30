# -*- coding: utf-8 -*-
import scrapy


class PttcrawlerSpider(scrapy.Spider):
    name = 'PTTCrawler'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Zastrology/M.1577350847.A.2E0.html']
    cookies = {'over18': '1'}

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies=self.cookies)    

    def parse(self, response):
        pass
