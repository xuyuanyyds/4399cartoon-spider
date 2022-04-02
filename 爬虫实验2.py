'''
import requests
import json
from pprint import pprint
def main():
    url="http://127.0.0.1/test1.json"
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
             "Referer":"http://www.baidu.com"

    }
    resp = requests.get(url=url,headers=headers)
    json_str=resp.content.decode("utf-8")
    print(json_str)
    retl=json.loads(json_str)
    print(retl["objects"][0]["EmailAddress"])
    #美化打印
    pprint(retl)

    pass


if __name__ == '__main__':
    main()



import requests
import json

def main():
    url="http://127.0.0.1/test1.json"
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
             "Referer":"http://www.baidu.com"

    }
    resp = requests.get(url=url,headers=headers)
    json_str=resp.content.decode("utf-8")
    print(json_str)
    ret1=json.loads(json_str)#loads是变成json类型的数据
    print(ret1)
    #保存一下
    
    with open("a.txt","w",encoding="utf-8") as f:
        #ensure_ascii=False可以显示中文，indent=2把子节点向后移2个空格
        f.write(json.dumps(ret1,ensure_ascii=False,indent=2))
    
    #读取本地json文件
    with open("a.txt","r",encoding="utf-8") as f:
        ret2=json.load(f)
        print(ret2)



    pass


if __name__ == '__main__':
    main()


import requests
import json
from bs4 import BeautifulSoup


def main():
    url = "http://www.4399dmw.com/donghua/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
        "Referer": "http://www.baidu.com"

        }
    resp = requests.get(url=url,headers=headers)
    #print(resp.content.decode("utf-8"))

    #保存页面源代码
    html_doc=resp.content.decode("utf-8")
    #使用bs去处理网页源代码
    soup=BeautifulSoup(html_doc)
    #找到class='m-hd'的div标签
    #print(soup.find('div',class_='m-hd')

    #找到所有的a标签并且class='u-card'的东西，放在list里，取出第几个
    #print(soup.find_all('a', class_='u-card')[2].get_text().strip())#strip()去掉空格，换行。

    #获取页面中有多少个这种元素
    #number=len(soup.find_all('a',class_='u-card'))
    #print(number)
    #for i in range(number)：
        #获取某个元素的文字内容
        #print(soup.find_all('a',class_='u-card')[i].get_text().strip())
        #提取网站所有文字
        #print(soup.get_text())
    #查找所有div下id='j-anime-nav-collect'的标签内容，放在一个list里
    #print(soup.select("div > #j-anime-nav-collect")[0].get_text())
    #print(soup.select("ul > .item")[0].get_text())
    #取出网页的标题，用get_text()也行
    #print(soup.title.string)

    #取出所有的img标签
    #print(soup.find_all('img'))
    #找到第一个class='u-tt'的，无视标签，get_text()是取出文字
    #print(soup.find(class_='u-tt').get_text())

    list = soup.find('div',class_='lst-item').find_all('a',class_='u-card')
    for item in list:
        #取出list中每一行的细节
        mingzi = item.find('p',class_='u-tt').get_text()
        #取出图片地址
        pic_url = item.find('img').get('data-src')
        print(mingzi+"----"+pic_url)

import requests
import json
from bs4 import BeautifulSoup

def main():
    url = "http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/"
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
            "Referer": "http://www.baidu.com"

        }
    resp = requests.get(url=url, headers=headers)
    # 保存页面源代码
    html_doc = resp.content.decode("utf-8")
    # 使用bs去处理网页源代码
    soup = BeautifulSoup(html_doc)

    list = soup.find('div', class_='lst').find_all('a', class_='u-card')
    for item in list:
        # 取出list中每一行的细节
        mingzi = item.find('p', class_='u-tt').get_text()
        # 取出图片地址
        pic_url = item.find('img').get('data-src')
        print(mingzi + "----" + pic_url)

    pass


if __name__ == '__main__':
    main()



import requests
import json
from bs4 import BeautifulSoup

def pachong(page):
    url = "http://www.4399dmw.com/search/dh-1-0-0-0-0-{}-0/".format(page)#让传进来的东西直接去修改它{}
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
            "Referer": "http://www.baidu.com"

        }
    resp = requests.get(url=url, headers=headers)
    # 保存页面源代码
    html_doc = resp.content.decode("utf-8")
    # 使用bs去处理网页源代码
    soup = BeautifulSoup(html_doc)

    list = soup.find('div', class_='lst').find_all('a', class_='u-card')
    for item in list:
        # 取出list中每一行的细节
        mingzi = item.find('p', class_='u-tt').get_text()
        # 取出图片地址
        pic_url = item.find('img').get('data-src')
        print(mingzi + "----" + pic_url)

def main():
    for i in range(14):
        print("爬虫爬到了第"+str(i)+"页")
        pachong(i)

    
    pass




if __name__ == '__main__':
    main()
'''


import requests
import json
from bs4 import BeautifulSoup


def pachong(page):
    url = "http://www.4399dmw.com/search/dh-1-0-0-0-0-{}-0/".format(page)  # 让传进来的东西直接去修改它{}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
        "Referer": "http://www.baidu.com"

    }
    resp = requests.get(url=url, headers=headers)
    # 保存页面源代码
    html_doc = resp.content.decode("utf-8")
    # 使用bs去处理网页源代码
    soup = BeautifulSoup(html_doc)

    list = soup.find('div', class_='lst').find_all('a', class_='u-card')
    for item in list:
        # 取出list中每一行的细节
        mingzi = item.find('p', class_='u-tt').get_text()
        # 取出图片地址
        pic_url = item.find('img').get('data-src')
        print(mingzi + "----" + pic_url)


def main():
    url="https://www.4399dmw.com/huoying/donghua/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
        "Referer": "http://www.baidu.com"

    }
    resp = requests.get(url=url, headers=headers)
    # 保存页面源代码
    html_doc = resp.content.decode("utf-8")
    # 使用bs去处理网页源代码
    soup = BeautifulSoup(html_doc)
    #print(soup.find_all('div',class_='works__info')[3])

    list = soup.find_all('div', class_='works__info')[3].find_all('a')
    for item in list:
        print(item.get_text())





    pass


if __name__ == '__main__':
    main()