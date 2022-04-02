'''import requests

def main():
    url = "https://www.4399dmw.com/search/dh-1-0-0-0-0-{}-0"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
               }#需要反爬虫侦测，要写很多。
    pass

    for i in range(14):
        urla = url.format(i)
        print(urla)
        resp = requests.get(url=urla,headers=headers)
        with open("a"+str(i)+".txt","wb+") as f:
            #写入文件
            f.write(resp.content)
    pass

if __name__ == '__main__':
    main()


import requests

def main():
    url = "https://www.4399dmw.com/search/dh-1-0-0-0-0-{}-0"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
               }
    #代理
    proxies = {"HTTP":"218.75.69.50:57903"}
    urla = url.format("1")
    print(urla)
    resp = requests.get(url=urla,headers=headers,proxies=proxies)
    with open("a.txt","wb+") as f:
        #写入文件
        f.write(resp.content)
    pass



if __name__ == '__main__':
    main()

import requests

def main():
    url = "http://sqlilabs.njhack.xyz/Less-20/index.php"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"


    }
    data ={"uname":"admin","passwd":"admin"}
    #实例化session
    sessions=requests.session()

    #发送post请求，提交用户名和密码
    resp = sessions.post(url,headers=headers,data=data)
          #print(resp) 若回复200说明请求成功.print(resp.content.decode("utf-8"))
    #此时session里面已经有cookie的信息了，可以直接用session去get登录的任何界面
    res = sessions.get(url,headers=headers)
    print(res.content.decode("utf-8"))
    
    pass

if __name__ == '__main__':
    main()


import requests


def main():
    url = "http://sqlilabs.njhack.xyz/Less-20/index.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"

        }
    cookie_dict = {"uname":"admin"}
    resp = requests.get(url,headers=headers,cookies=cookie_dict)
    print(resp.content.decode("utf-8"))


    pass


if __name__ == '__main__':
    main()



import requests


def main():
    url = "http://sqlilabs.njhack.xyz/Less-20/index.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
        "Cookie":"uname=admin"
        }

    resp = requests.get(url,headers=headers)
    print(resp.content.decode("utf-8"))


    pass


if __name__ == '__main__':
    main()


import requests
from retrying import retry
@retry(stop_max_attempt_number=3)
def qingqiu(inurl):
    url=inurl
    print("开始请求网站")
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"

    }
    res = requests.get(url=url,headers=headers)
    with open("a.txt","wb+")as f:
        f.write(res.content.decode("utf-8"))
        print("请求成功")
    pass

def main():
    try:
        qingqiu("http://www.4399dmw.comx/search/dh-1-0-0-0-0-1-0/")
    except:
        print("no")
    pass


if __name__ == '__main__':
    main()


import requests
import json

def main():
    url="https://json.tewx.cn/user/API_kdd531mytfdzm06i?sdAS1dsnuUa3sd=190001&Jsdh4bajs99dii=sohpuisypf4nfaei"
    resp=requests.get(url=url)
    #print(resp.content.decode("utf-8"))
    content=resp.content.decode("utf-8")
    print(type(content))
    #把字符串变成字典，有了字典就能查东西了。
    shuju=json.loads(content)
    print(type(shuju))
    print(shuju)
    print(shuju["code"])
    print(shuju["data"]["JSON"]["mydata"]["name"])



    pass


if __name__ == '__main__':
    main()
'''

