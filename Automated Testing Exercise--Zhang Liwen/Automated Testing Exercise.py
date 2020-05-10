from selenium import webdriver
from selenium.webdriver import ActionChains
import os, time
def main():
    chrome_driver =r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe'
    driver= webdriver.Chrome(executable_path=chrome_driver)   # 调用Chrome()类
    driver.get("https://image.baidu.com/")  # 访问百度首页
    driver.find_element_by_id("kw").send_keys("小青蛙")# 输入"Selenium"
    driver.find_element_by_class_name('s_search').click()
    windows = driver.window_handles
    driver.switch_to.window(windows[0])
    time.sleep(5)
    driver.find_element_by_name('pn3').click()
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    driver.get_screenshot_as_file("D:\demo\demo.png")
if __name__=='__main__':
     main()