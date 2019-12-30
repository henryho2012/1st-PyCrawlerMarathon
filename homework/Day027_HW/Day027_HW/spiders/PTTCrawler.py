# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from Day027_HW.items import Day027HwItem as Item

class PttcrawlerSpider(scrapy.Spider):
    name = 'PTTCrawler'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Zastrology/M.1577350847.A.2E0.html']
    cookies = {'over18': '1'}

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies=self.cookies)    

    def parse(self, response):
        item = response.css('span[class="article-meta-value"]::text').extract()
        createItem = Item()
        createItem['author'] = item[0]
        createItem['plate'] = item[1]
        createItem['title'] = item[2]
        createItem['creatTime'] = item[3]
        return createItem
