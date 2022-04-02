'''
import requests
from selenium import  webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


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

    #使用get方法打开一个网站
    driver.get("http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/")

    #拖拽操作
    first_tar = driver.find_element(By.XPATH,"//p[contains(text(),'吃鸡大作战')]")
    second_tar = driver.find_element(By.XPATH,"//p[contains(text(),'鬼灭之刃')]")
    action = ActionChains(driver)
    action.drag_and_drop(first_tar, second_tar).perform()


    time.sleep(6)
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
    mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
    # 使用某个手机型号浏览
    #options.add_experimental_option('mobileEmulation', mobileEmulation)

    driver = webdriver.Chrome("C:\python\chromedriver.exe", options=options)

    #使用get方法打开一个网站
    #driver.get("http://127.0.0.1/")
    #处理弹窗
    #driver.switch_to.alert.accept()
    #鼠标点击像素操作
    #ActionChains(driver).move_by_offset(500,90).click().key_down("蜡").perform()
    #ActionChains(driver).move_by_offset(500, 90).click().key_up("蜡").perform()
    #ActionChains(driver).move_by_offset(0,0).perform()
    #ele = driver.find_element_by_xpath("//p[contains(text(),'吃鸡大作战')]")
    #ActionChains(driver).move_to_element(ele).context_click().perform()

    #ActionChains(driver).move_to_element_with_offset(ele,300,0).context_click().perform()





    #js = 'window.open("http://www.baidu.com/")'
    #driver.execute_script(js)
    #print(driver.current_url)
    #driver.switch_to.window(driver.window_handles[1])
    #print(driver.current_url)
    #driver.switch_to.window(driver.window_handles[0])
    #print(driver.current_url)
    #print(driver.window_handles)

    driver.get("http://www.4399dmw.com/search/dh-1-0-0-0-0-0-0/")
    res = driver.find_elements_by_xpath("//div[@class='u-ct']")
    for i in range(len(res)):
        title = res[i].find_element_by_xpath("./p[@class='u-tt']").get_attribute('innerText')
        print(title)




    time.sleep(5)
    # 关闭webdriver
    driver.quit()
    pass


if __name__ == '__main__':
    main()