import requests
from bs4 import  BeautifulSoup
import lxml

url='http://gz.meituan.com/shop/2949'
try:
    headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    web_data=requests.get(url,headers = headers)
    web_data.encoding='utf-8'
    content=web_data.text
    soup = BeautifulSoup(content, 'lxml')
    # print (soup)
    # can = soup.select('p[class="under-tit]')
    # can =soup.find_all('span',class_='geo')
    can =soup.find_all('div',class_="fs-section__left")
    print (can)
    for i in can:
        print (i.get_text().strip().split('\n'))

except Exception as e:
    print(e)