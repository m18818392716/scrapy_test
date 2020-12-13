import scrapy
from bs4 import BeautifulSoup
from SpiderObject.items import CityItem

class HotelSpider(scrapy.Spider):
    # 爬虫名称
    name = 'hotel'
    # 爬虫的可信域名
    allowed_domains = ['bnb.qunar.com']
    # 爬虫的url集合
    start_urls = ['http://bnb.qunar.com/hotcity.jsp']
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
        div_b_allcity = soup.find('div', class_='b_allcity')
        # 实例化一个item
        item = CityItem()
        # 判断是否存在此盒子
        # 其实这里也可以不用加这个判断，因为他是肯定存在的，我这里加上去算是培养自己的一个习惯吧
        if div_b_allcity is not None:
            # 找到所有class="e_city_name clr_after"的div
            #
            for div_cityItem in div_b_allcity.find_all('div'):
                # 跟上面判断一样
                if div_cityItem is not None:
                    ul = div_cityItem.find('ul')
                    if ul is not None:
                        for li_item in ul.find_all('li'):
                            # 跟上面判断一样
                            if li_item is not None:
                                # 获取城市名称
                                item['name'] = li_item.find('a').get_text()
                                # 获取城市对应url
                                item['url'] = li_item.find('a').get('href')
                                print(item)
        pass