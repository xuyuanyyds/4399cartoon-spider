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
    mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
    # 使用某个手机型号浏览
    #options.add_experimental_option('mobileEmulation', mobileEmulation)

    driver = webdriver.Chrome("C:\python\chromedriver.exe", options=options)


    driver.get("http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/")

    #拖动滑块到底部
    #js = "document.documentElement.scrollTop = 10000"
    #driver.execute_script(js)

    #页面截图
    #driver.get_screenshot_as_file("./abc.jpg")

    #指定位置截图
    #pic = driver.find_element_by_xpath("//div[@class='lst']/a[3]")
    #pic.screenshot('./chiji.png')
    #time.sleep(1)
    #driver.get("http://www.4399dmw.com/dh/cjdzz/")

    #浏览器后退，刷新和前进
    #driver.back()
    #time.sleep(2)
    #driver.refresh()
    #time.sleep(2)
    #driver.forward()

    #最大化
    #driver.maximize_window()
    
    



    time.sleep(5)
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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def web():
    # 指定调用某个地方第chrome
    options = webdriver.ChromeOptions()
    # chromium浏览器第主程序位置
    location = r"C:\python\chrome-win\chrome.exe"
    # 在options增加读取位置
    options.binary_location = location
    # 设置手机型号
    mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
    # 使用某个手机型号浏览
    # options.add_experimental_option('mobileEmulation', mobileEmulation)
    #某些网站会识别selenium
    options.add_experimental_option('excludeSwitches',['enable-automation'])
    #添加user_agent
    #options.add_argument('User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')
    #图片不加载
    prefs = {
        'profile.default_content_setting_values':{
            'images':2
        }
    }
    options.add_experimental_option('prefs',prefs)

    driver = webdriver.Chrome("C:\python\chromedriver.exe", options=options)

    #如果2s页面还没有加载出来，就抛出一个异常，需要配合try来做
   # driver.set_page_load_timeout(1)
    #driver.get("http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/")
    driver.get("http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/")
    #隐形等待，有些网站的内容加载需要等一下，全局做一次就行了
    #driver.implicitly_wait(10)

    #a = WebDriverWait(driver,20).until(EC.text_to_be_present_in_element((By.XPATH,"//div[@class='lst']/a[3]/div/p"),u'吃鸡大作战'))
    #print(a)

    #pic = driver.find_element_by_xpath("//div[@class='lst']/a[3]")
    #pic.screenshot('./chiji.png')

    target1 = driver.find_element_by_xpath("//div[@class='lst']/a[1]")
    ActionChains(driver).click(target1).perform()

    driver.switch_to.window(driver.window_handles[0])
    target2 = driver.find_element_by_xpath("//div[@class='lst']/a[2]")
    ActionChains(driver).click(target2).perform()

    driver.switch_to.window(driver.window_handles[1])
    #关闭切到第标签
    driver.close()

    time.sleep(8)
    # 关闭webdriver
    driver.quit()
    pass


def main():
    try:
        web()
    except:
        print("页面太慢了")
    pass


if __name__ == '__main__':
    main()