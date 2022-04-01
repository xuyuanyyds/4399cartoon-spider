# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import os
from urllib import request


class Test1Pipeline:
    #打开爬虫的时候执行
    def open_spider(self,spider):
        #打开并准备存储
        self.fp = open("spider1.json","w",encoding='utf-8')
        #判断路径是否存在
        self.path= os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        pass


    #使用yield的时候执行
    def process_item(self, item, spider):
        item_json = json.dumps(dict(item),ensure_ascii=False)
        self.fp.write(item_json+'\n')
        #获得item的细节
        #print(item)#{'title':['xxxxx'],'pic':['yyyy']}
        title = item['title'][0]
        pic = item['pic'][0]
        path1 = os.path.join(self.path,'pic1')
        if not os.path.exists(path1):
            os.mkdir(path1)
        #下载图片并且加上jpg后缀名
        request.urlretrieve(pic,os.path.join(path1,title+'.jpg'))
        return item

    #爬虫结束的时候执行
    def close_spider(self,spider):
        #结束关闭文件
        self.fp.close()
        pass
