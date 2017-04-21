#coding:utf-8
import requests
from bs4 import BeautifulSoup
import time,json
from lxml import etree
from selenium import webdriver
# all_url=['http://gz.meituan.com/category/meishi?mtt=1.index%2Fdefault%2Fpoi.0.0.j1pon2s6',
# 'http://gz.meituan.com/category/meishi/all/page2?mtt=1.index%2Fdefault%2Fpoi.0.0.j1pom9qr',
# 'http://gz.meituan.com/category/meishi/all/page3?mtt=1.index%2Fdefault%2Fpoi.0.0.j1polefb',
# 'http://gz.meituan.com/category/meishi/all/page4?mtt=1.index%2Fdefault%2Fpoi.0.0.j1pojice',
# 'http://gz.meituan.com/category/meishi/all/page5?mtt=1.index%2Fdefault%2Fpoi.0.0.j1pohco3',
# 'http://gz.meituan.com/category/meishi/all/page6?mtt=1.index%2Fdefault%2Fpoi.0.0.j1poiq1x']
# url='http://gz.meituan.com/category/meishi/all/page{0}?mtt=1.index%2Fdefault%2Fpoi.0.0'.format(page)
all_link=[]
all_name=[]
def fetch(page):
    # PROXY = "121.206.16.147:23650"#use proxy
    options = webdriver.ChromeOptions()
    # chrome_options = webdriver.ChromeOptions()
    # options.add_argument('--proxy-server={0}'.format(PROXY))

    # 设置中文
    options.add_argument('lang=zh_CN.UTF-8')
    # 更换头部
    options.add_argument(
        'user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
    url = 'http://gz.meituan.com/category/qitameishi/all/page{0}?mtt=1.index%2Fdefault%2Fpoi.0.0.'.format(page)
    driver = webdriver.Chrome(chrome_options=options)  # 用chrome浏览器打开
    driver.get(url)
    time.sleep(5)
    for i in range(2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
    try:
        # headers = {'Accept':'*/*',
        # 'Accept-Encoding':"gzip, deflate",
        # 'Accept-Language':"en-US,en;q=0.8",
        # 'Connection':'keep-alive',
        # 'Content-Length':'5137',
        # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie':'ci=20; abt=1492605604.0%7CBCF; em=bnVsbA; om=bnVsbA; ppos=23.119737%2C113.611222; pposn=%E4%BA%9A%E4%BF%A1%E5%8F%8C%E7%9A%AE%E5%A5%B6; __mta=142450189.1492634404259.1492642814582.1492643045947.11; __utma=211559370.641137971.1492634404.1492638006.1492640447.3; __utmb=211559370.8.9.1492640646579; __utmc=211559370; __utmz=211559370.1492634404.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=211559370.|1=city=gz=1; uuid=f15d0b7fef1ea7261b19.1492605604.0.0.0; oc=hbIuqsHXtKbmk6rQUJ9xmewMeUmV3EWgQ89qYNfG26P2NonIJStDbWYQQLpiPtY07cH9jfyb45UJWBmx_WkpnqqzmRP0j1ihbEo9GY_yXLG-l-pAhvu2C6BQ2wBWcTHfKQrbNjzVutTq4J8Z2q3-jJtHUsvDcG3U4pmd4RXA_IQ',
        # 'Host':'gz.meituan.com',
        # 'Origin':'http://gz.meituan.com',
        # 'Referer':"http://gz.meituan.com/category/meishi/all/page2?mtt=1.index%2Fdefault%2Fpoi.0.0.j1pjkz9x",
        # 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        # 'X-Requested-With':'XMLHttpRequest'
        # }
        #
        # url ='http://gz.meituan.com/category/meishi/all/page{0}?mtt=1.index%2Fdefault%2Fpoi.0.0.j1pjkz9x'.format(page)
        # web_data=requests.post(url,headers = headers)
        # web_data.encoding='utf-8'
        # content=web_data.text
        html = driver.page_source
        soup=BeautifulSoup(html,'lxml')
        can =soup.find_all("a", class_="link f3 J-mtad-link")
        for i in can:
            all_link.append(i.get('href'))
            all_name.append(i.get_text())
        driver.close()
    except Exception as e:
        print (e)

        # with open('meituan.csv', 'a')as f:
        #     writer = csv.writer(f)
        #     for link, name in zip(all_link, all_name):
        #         writer.writerow(link+name)
def write_file():
    with open('meituan_url.txt', 'a')as f:
        for link in all_link:
            f.write(link+'\n')




if __name__=='__main__':
    for url in range(1,8):
        fetch(url)
    write_file()