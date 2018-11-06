
import scrapy
import re

from ..items import TanqinbaItem

class TanqinbaSpider(scrapy.Spider):
    name = "tanqinba"
    allowed_domains = ["tan8.com"]
    start_urls = ['http://www.tan8.com/yuepu-%s.html' % x for x in range(0,70000)]


    def parse(self, response):
        # 获取所有图片的a标签
        print('---------parse--------')
        #定义正则表达式：一段中文中取数字
        pattern = re.compile(r'[^\d]*(\d+)[^\d]*')

        item = TanqinbaItem()
        item['url'] = response.url
        item['name'] = response.xpath('//div[@class="yuepu_name_0421"]/h1[@class="title_color"]/text()').extract()[0]
        item['singer'] = response.xpath('//div[@class="yuepu_name_0421"]//a/i/text()').extract()[0]
        item['seeNum'] = re.findall(pattern,response.xpath('//div[@class="yuepu_name_0421"]//span[@class="brief_color eyes"]/text()').extract()[0])[0]
        item['des'] = response.xpath('//p[@class="brief_0421 content_color"]/text()').extract()[0]
        item['collectNum'] = re.findall(pattern,response.xpath('//div[@class="yuepu_name_0421"]//span[@class="brief_color xin c-num"]/text()').extract()[0].split("次")[0])[0]
        item['hard'] = re.findall(pattern,response.xpath('//div[@class="yuepu_name_0421"]//span[@class="brief_color"]/text()').extract()[1])[0]
        commentUserList = response.xpath('//ul[@class="liuyanList_0421"]//div[@class="text"]//a[@class="href"]/text()').extract()
        commentDateList = response.xpath('//ul[@class="liuyanList_0421"]//div[@class="text"]//p[@class="time brief_color"]/text()').extract()
        commentContentList = response.xpath('//ul[@class="liuyanList_0421"]//div[@class="text"]//p[@class="msg_1125 title_color"]/text()').extract()

        item['commentUser'] = '###'.join(commentUserList)
        item['commentDate'] = '###'.join(commentDateList)
        item['commentContent'] = '###'.join(commentContentList)
        try:
            item['user'] = response.xpath('//div[@class="col_243"]//h3[@class="title_color"]/text()').extract()[0]
        except IndexError as e:
            item['user'] = '未定义'
        item['time'] = response.xpath('//div[@class="col_243"]//p[@class="brief_color"]/text()').extract()[1]

        # 返回爬取到的数据
        yield item