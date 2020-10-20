#coding=utf-8
 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from PIL import Image
from PIL import ImageEnhance
import unittest, time, re
import pytesseract
 
class lgoin(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(10)
    self.base_url = "https://www.nextpair.com/admin#/login" # 要测试的链接
    self.title = 'NextPair admin' # 测试网站的Title
    self.verificationErrors = []
    self.accept_next_alert = True
 
  def test_lgoin(self):
    driver = self.driver
    try:
        driver.get(self.base_url)
    finally:
        driver.maximize_window()
        driver.save_screenshot('All.png') # 截取当前网页，该网页有我们需要的验证码
        imgelement = driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/div/div/div/img')
        rangle = (984, 517, 1159, 562) # 写成我们需要截取的位置坐标
        i = Image.open("All.png") # 打开截图
        result = i.crop(rangle) # 使用Image的crop函数，从截图中再次截取我们需要的区域
        size = (350, 90)
        image01 = result.convert('RGB').resize(size).save('result.jpg')
        text = pytesseract.image_to_string(img).strip()
        print(text)

    assert self.title in driver.title

'''
    driver.find_element_by_xpath('//*[@id="login"]/form/div[1]/div/div/input').send_keys('hi@nextpair.com') # 用户名
    driver.find_element_by_xpath('//*[@id="login"]/form/div[2]/div/div/input').send_keys('hellonextpair') # 密码
    #driver.find_element_by_name('verifyCode').clear()
    driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/div/div/input').send_keys(text)
    driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/div/button[1]').click()
'''

if __name__ == "__main__":
  unittest.main()

