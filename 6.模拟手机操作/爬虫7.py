'''
from selenium import webdriver
import time
from selenium.webdriver.common.touch_actions import TouchActions


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
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    #关闭w3c模式！！非常重要，否则无法点击
    options.add_experimental_option('w3c',False)
    driver = webdriver.Chrome("C:\python\chromedriver.exe", options=options)

    driver.get("http://www.4399dmw.com/donghua/")
    # 点击坐标操作
    #action = TouchActions(driver)
    #action.tap_and_hold(50, 125).release(50, 125).perform()
    
    




    time.sleep(5)
    driver.quit()
    pass

if __name__ == '__main__':
    main()
'''
from selenium import webdriver
import time
from selenium.webdriver.common.touch_actions import TouchActions


def main():
    # 指定调用某个地方第chrome
    options = webdriver.ChromeOptions()
    # chromium浏览器第主程序位置
    location = r"C:\python\chrome-win\chrome.exe"
    # 在options增加读取位置
    options.binary_location = location

    driver = webdriver.Chrome("C:\python\chromedriver.exe", options=options)

    driver.get("http://www.4399dmw.com/donghua/")
    time.sleep(5)
    sell1 = driver.find_element_by_xpath("//input[@id='j-input']")
    driver.execute_script("arguments[0].value='';",sell1)






    time.sleep(5)
    driver.quit()
    pass


if __name__ == '__main__':
    main()