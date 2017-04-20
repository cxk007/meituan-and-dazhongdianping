#coding:utf-8
# from selenium import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get("http://gz.meituan.com/category/meishi?mtt=1.index%2Fdefault%2Fpoi.0.0.j1pi4mmp")
browser.find_element_by_id("yui_3_16_0_1_1492640024987_2899").click()
browser.close()
# print (driver.page_source)