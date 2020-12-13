#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/13 20:21
# @Author  : Susanna
# @Email   : m18818392716@163.com
# @File    : toutiao.py
# @Software: PyCharm

import scrapy
from bs4 import BeautifulSoup
from SpiderObject.items import NewsItem

class ToutiaoSpider(scrapy.Spider):
    # 爬虫名称
    name = 'toutiao'
    # 爬虫的可信域名
    allowed_domains = ['www.toutiao.com']
    # 爬虫的url集合
    start_urls = ['http://www.toutiao.com/ch/news_hot']
    # 解析html获取所需数据
    def parse(self, response):
        '''
        解析html获取所需数据
        :param response:
        :return:
        '''
        # 爬取下来的代码
        html = response.text
        soup = BeautifulSoup(html, "lxml")
        # 获取包裹所有数据的div
        div_b_allcity = soup.find('div', class_='feed-list')
        # 实例化一个item
        item = NewsItem()
        # 判断是否存在此盒子
        # 其实这里也可以不用加这个判断，因为他是肯定存在的，我这里加上去算是培养自己的一个习惯吧
        if div_b_allcity is not None:
            # 找到所有class="e_city_name clr_after"的div
            #
            for div_cityItem in div_b_allcity.find_all('div', class_='single-mode'):
                # 跟上面判断一样
                if div_cityItem is not None:
                    imgsrc = div_cityItem.find('div', class_='single-mode-lbox')
                    title = div_cityItem.find('div', class_='single-mode-rbox')
                    if imgsrc is not None:
                        # 获取城市名称
                        item['imgsrc'] = imgsrc.find('img', class_='lazy-load-img').get('src')
                    if imgsrc is not None:
                        # 获取城市对应url
                        item['title'] = title.find('a', class_='link').get_text()
                    print(item)
        pass