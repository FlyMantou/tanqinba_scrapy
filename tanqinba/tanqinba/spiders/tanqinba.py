
import scrapy

from ..items import TanqinbaItem

class TanqinbaSpider(scrapy.Spider):
    name = "tanqinba"
    allowed_domains = ["tan8.com"]
    start_urls = ['http://www.tan8.com/yuepu-%s.html' % x for x in range(0,70000)]


    def parse(self, response):
        # 获取所有图片的a标签
        print('---------parse--------')
        item = TanqinbaItem()
        item['url'] = response.url
        item['name'] = response.xpath('//div[@class="yuepu_name_0421"]/h1[@class="title_color"]/text()').extract()[0]
        item['singer'] = response.xpath('//div[@class="yuepu_name_0421"]//a/i/text()').extract()[0]
        item['seeNum'] = response.xpath('//div[@class="yuepu_name_0421"]//span[@class="brief_color eyes"]/text()').extract()[0]
        item['des'] = response.xpath('//p[@class="brief_0421 content_color"]/text()').extract()[0]
        item['collectNum'] = response.xpath('//div[@class="yuepu_name_0421"]//span[@class="brief_color xin c-num"]/text()').extract()[0]
        item['hard'] = response.xpath('//div[@class="yuepu_name_0421"]//span[@class="brief_color"]/text()').extract()[1]
        try:
            item['user'] = response.xpath('//div[@class="col_243"]//h3[@class="title_color"]/text()').extract()[0]
        except IndexError as e:
            item['user'] = '未定义'
        item['time'] = response.xpath('//div[@class="col_243"]//p[@class="brief_color"]/text()').extract()[1]

        # 返回爬取到的数据
        yield item