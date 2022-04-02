'''
import requests
from selenium import  webdriver
import time



def main():

    #指定调用某个地方第chrome
    options = webdriver.ChromeOptions()
    #chromium浏览器第主程序位置
    location = r"C:\python\chrome-win\chrome.exe"
    #在options增加读取位置
    options.binary_location = location
    driver = webdriver.Chrome("C:\python\chromedriver.exe",options=options)

    #使用get方法打开一个网站
    driver.get("http://www.4399dmw.com/donghua/")

    #根据id找到对应第目标，并且输入什么内容
    driver.find_element_by_id("j-input").send_keys("蜡笔")

    #找到按钮
    driver.find_element_by_xpath("//button[@class='banner__btn']").click()

    #获取当前页面地址(尚未切换标签)
    print(driver.current_url)


    time.sleep(5)
    # 关闭webdriver
    driver.quit()
    pass


if __name__ == '__main__':
    main()


import requests
from selenium import  webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains




def main():

    #指定调用某个地方第chrome
    options = webdriver.ChromeOptions()
    #chromium浏览器第主程序位置
    location = r"C:\python\chrome-win\chrome.exe"
    #在options增加读取位置
    options.binary_location = location
    # 设置手机型号
    mobileEmulation = {'deviceName': 'iPhone 6/7/8 Plus'}
    # 使用某个手机型号浏览
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    # 使用静默模式
    #options.add_argument("headless")
    # 加代理http https socks4 socks5

    #更改浏览器语言

    driver = webdriver.Chrome("C:\python\chromedriver.exe",options=options)

    #使用get方法打开一个网站
    driver.get("http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/")

    #time.sleep(2)
    #刷新页面
    #driver.refresh()

    #点击下一页
    #driver.find_element_by_xpath("//a[@class='next']").click()

    #移动鼠标第位置
    action = ActionChains(driver).move_by_offset(50,125).click()
    #开始执行
    action.perform()
    #鼠标移回来并且开始执行
    ActionChains(driver).move_by_offset(-50,125).perform()







    time.sleep(8)
    # 关闭webdriver
    driver.quit()
    pass


if __name__ == '__main__':
    main()
'''



import requests
from selenium import  webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains




def main():

    #指定调用某个地方第chrome
    options = webdriver.ChromeOptions()
    #chromium浏览器第主程序位置
    location = r"C:\python\chrome-win\chrome.exe"
    #在options增加读取位置
    options.binary_location = location
    # 设置手机型号
    mobileEmulation = {'deviceName': 'iPhone 6/7/8 Plus'}
    # 使用某个手机型号浏览
    #options.add_experimental_option('mobileEmulation', mobileEmulation)
    # 使用静默模式
    #options.add_argument("headless")
    # 加代理http https socks4 socks5

    #更改浏览器语言

    driver = webdriver.Chrome("C:\python\chromedriver.exe",options=options)

    #使用get方法打开一个网站
    driver.get("http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/")
    #html = driver.find_element_by_xpath("//a[@class='next']").get_attribute("outerHTML")
    #print(html)

    #获取登录的位置，发现一个是link的，文字是text的element
    #denglu = driver.find_element_by_link_text("登录")
    #鼠标悬停
    #ActionChains(driver).move_to_element(denglu).perform()

    #找到logo的位置
    logo = driver.find_element_by_xpath("//a[@class='banner__logo']")
    denglu = driver.find_element_by_xpath("//a[contains(text(),'登录')]")
    #执行点击
    action = ActionChains(driver)
    action.click(logo)
    time.sleep(3)
    action.click(denglu)
    action.perform()

    #执行点击
    #ActionChains(driver).click(logo).perform()




    time.sleep(7)
    # 关闭webdriver
    driver.quit()
    pass
'''
    for page in range(14):
        print("开始爬行到第"+str(page)+"页")
        res = driver.find_elements_by_xpath("//div[@class='lst']/a/div/p")
        for i in range(len(res)):
            print(res[i].text)
        #点到下一页
        driver.find_element_by_xpath("//a[@class='next']").click()
'''









if __name__ == '__main__':
    main()




