import scrapy
from test1.items import Test1Item

class Spider1Spider(scrapy.Spider):
    #爬虫根据这个名字运行
    name = 'spider1'
    #允许第域名
    allowed_domains = ['4399dmw.com']
    #从什么域名开始
    start_urls = ['http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/']

    def parse(self, response):
        datas_pic = response.xpath("//a[@class='u-card']/img")
        for item in datas_pic:
        #使用items来存储
            pic = item.xpath("@data-src").extract()
            title = item.xpath("@alt").extract()
            topipeline1 = Test1Item(pic=pic,title=title)
            yield topipeline1


    pass
        #找到下一页第链接
        #next_url = response.xpath("//a[@class='next']/@href").get()
        #if not next_url:
        #    return
        #else:
            #让他返回继续执行这个方法
        #    yield scrapy.Request("http://www.4399dmw.com/"+next_url,callback=self.parse)
        #pass
