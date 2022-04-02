4399动漫网爬虫系列🚀
--------


[1、爬虫1](https://github.com/xuyuanyyds/4399cartoon-spider/tree/main/%E7%88%AC%E8%99%AB1)

* 代理使用：是一种反反爬虫的手段，利用cookie，session，user-agent，referer，header等参数
* 使用不同的user-agent
随机生成uers-agent来反爬虫

> 处理session（用户登录维持）
>
> 有的网站内部的情况需要登陆之后带着cookie/session信息才能访问

* 处理cookie直接登录的情况

 > 直接带着cookie请求

* retrying模块

> pip install retrying

* pip install retrying

> 爬虫不一定整站爬行，还可以请求接口
-----
[2.json数据处理及beautifulsoup](https://github.com/xuyuanyyds/4399cartoon-spider/tree/main/2.json%E6%95%B0%E6%8D%AE%E5%A4%84%E7%90%86%E5%8F%8Abeautifulsoup)


```
pip install bs4----安装bs4
```

* 加载json的数据

* ==Beautiful Soup==代替正则表达式

  1.使用bs处理网页源代码

  2.找到相应的标签

  3.获取此元素

* 解析网页的源码
-------------
[3.xpath以及selenium使用](https://github.com/xuyuanyyds/4399cartoon-spider/tree/main/3.xpath%E4%BB%A5%E5%8F%8Aselenium%E4%BD%BF%E7%94%A8)

* xpath

  ```
  pip install lxml
  
  from lxml import etree
  ```

  获取网页源码后，使用etree去转化为一个html对象

  此时element对象可以使用xpath语法

* xpath语法(<u>**部分**</u>)

  > //a _当前html页面中所有的a标签
  > 
  > //a/@href—— 当前html页面中所有a标签中的href的属性内容
  > 
  > //a/text()——当前html页面中所有a标签中的文本内容
  > 
  > //img/@src ——拿到所有img标签中的src的内容
  > 
  > //a//img/@src ——拿到所有a标签下面的所有img标签中的src内容

* selenium

```
pip install selenium
```
-----------
[4.复杂操作及selenium](https://github.com/xuyuanyyds/4399cartoon-spider/tree/main/4.%E5%A4%8D%E6%9D%82%E6%93%8D%E4%BD%9C%E5%8F%8Aselenium)

* 调用本地的chrome模拟人类操作

* 配合xpath找到对应内容

* 设置手机型号模拟操作

* 引入键盘鼠标操作

  ```
  from selenium.webdriver.common.keys import Keys
  from selenium.webdriver.common.action_chains import ActionChains
  ```
---------
[5.模拟人类操作](https://github.com/xuyuanyyds/4399cartoon-spider/tree/main/5.%E6%A8%A1%E6%8B%9F%E4%BA%BA%E7%B1%BB%E6%93%8D%E4%BD%9C)

* 配合xpath进行拖拽操作
* 鼠标点击像素操作
* 鼠标其他操作（**部分**）

```
click() ——点击鼠标左键
click_and_hold() ——点住鼠标左键不放
context_click() ——点击鼠标右键
double_click() ——双击鼠标左键
drag_and_drop_by_offset(first_tar,100,100) ——拖拽到某个坐标然后松开
key_down("a") ——按下一个键
key_up("a") ——抬起一个键
move_to_element(ele) ——移动到某个元素的位置
move_to_element_with_offset(ele,100,0) ——移动到某个元素的相对xx的位置（以找到元素的左上角作为0）
```

* 处理弹窗

* js😔新建标签页

* 切换标签页

  





