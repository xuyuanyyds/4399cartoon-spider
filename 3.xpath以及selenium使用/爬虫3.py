'''
import requests
from lxml import etree



def main():
    url ="http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/"
    headers ={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"

    }
    resp =requests.get(url=url,headers=headers)
    #获得网页源码
    html_doc = resp.content.decode("utf-8")
    #使用etree去转化html_doc,转化为一个html的对象，此时element对象可以使用xpath语法
    html=etree.HTML(html_doc)
    #print(html.xpath("//div[@class='u-ct']/p[@class='u-tt']/text()"))
    dongmantitle = html.xpath("//div[@class='u-ct']/p[@class='u-tt']/text()")
    dongmanpic = html.xpath("//div[@class='lst']/a/img/@data-src")
    print(dongmantitle)
    print(dongmanpic)


    pass


if __name__ == '__main__':
    main()
    
import requests
from lxml import etree

#页面内爬虫
def pachong(url):
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"

    }
    resp = requests.get(url=url, headers=headers)
    # 获得网页源码
    html_doc = resp.content.decode("utf-8")
    # 使用etree去转化html_doc,转化为一个html的对象，此时element对象可以使用xpath语法
    html = etree.HTML(html_doc)
    # print(html.xpath("//div[@class='u-ct']/p[@class='u-tt']/text()"))
    dongmantitle = html.xpath("//div[@class='u-ct']/p[@class='u-tt']/text()")
    dongmanpic = html.xpath("//div[@class='lst']/a/img/@data-src")
    print(dongmantitle)
    print(dongmanpic)


    pass
#发现下一页的爬虫
def find_next_page(url):
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"

    }
    resp = requests.get(url=url, headers=headers)
    # 获得网页源码
    html_doc = resp.content.decode("utf-8")
    # 使用etree去转化html_doc,转化为一个html的对象，此时element对象可以使用xpath语法
    html = etree.HTML(html_doc)
    # 获得下一页第链接
    next_page = html.xpath("//a[contains(text(),'下一页')]/@href")
    # 创建完整第链接
    really_next_page = "http://www.4399dmw.com" + next_page[0]
    # print(really_next_page)

    return really_next_page



def main():
    url = "http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/"


    while True:
        try:
            print("开始爬行的url:" +url)
            pachong(url)
            url = find_next_page(url)

        except:
            break

    print("最后一页爬完了")





    pass


if __name__ == '__main__':
    main()
    
'''



import requests
from lxml import etree
import random


#页面内爬虫
def pachong(url):
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"

    }
    resp = requests.get(url=url, headers=headers)
    # 获得网页源码
    html_doc = resp.content.decode("utf-8")
    # 使用etree去转化html_doc,转化为一个html的对象，此时element对象可以使用xpath语法
    html = etree.HTML(html_doc)
    # print(html.xpath("//div[@class='u-ct']/p[@class='u-tt']/text()"))
    dongmantitle = html.xpath("//div[@class='u-ct']/p[@class='u-tt']/text()")
    dongmanpic = html.xpath("//div[@class='lst']/a/img/@data-src")
    print(dongmantitle)
    print(dongmanpic)


    pass
#发现下一页的爬虫
def find_next_page(url):
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"

    }
    resp = requests.get(url=url, headers=headers)
    # 获得网页源码
    html_doc = resp.content.decode("utf-8")
    # 使用etree去转化html_doc,转化为一个html的对象，此时element对象可以使用xpath语法
    html = etree.HTML(html_doc)
    # 获得下一页第链接
    next_page = html.xpath("//a[contains(text(),'下一页')]/@href")
    # 创建完整第链接
    really_next_page = "http://www.4399dmw.com" + next_page[0]
    # print(really_next_page)

    return really_next_page



def main():
    version_id = random.randint(50,100)
    os_type = ['Windows NT 10.0','Windows NT 6.1','linux 10.0']


    ua ="Mozilla/5.0 ("+random.choice(os_type)+"; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103."+str(version_id)+" Safari/537.36"
    print(ua)
    pass


if __name__ == '__main__':
    main()