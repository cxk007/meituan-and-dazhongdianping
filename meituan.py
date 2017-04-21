import requests
from bs4 import  BeautifulSoup
from get_proxy import *
from multiprocessing import Pool
import lxml,time
all_url=[]
cont=[]
proxie=['112.85.87.12:30834',
'221.229.18.164:40582',
'183.144.205.23:17574',
'175.155.68.235:57347',
'59.39.128.98:45164']
proxies = [{'http': 'http://' + p} for p in proxie]
print (proxies)
with open('meituan_url.txt','r')as f:
    for i in f:
        url=i.strip('\n')
        all_url.append(url)
# print (all_url)
# url='http://gz.meituan.com/shop/2949'
def fetch(url):
    try:
        headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
        }
        web_data=requests.get(url,headers = headers)
        print (web_data.status_code)
        time.sleep(60)
        web_data.encoding='utf-8'
        content=web_data.text
        soup = BeautifulSoup(content, 'lxml')
        # print (soup)
        # can = soup.select('p[class="under-tit]')
        # can =soup.find_all('span',class_='geo')
        can =soup.find_all('div',class_="fs-section__left")
        print (can)
        for i in can:
            with open('meituan_all.txt', 'a') as f_out:
                for i in cont:
                    a=(i.get_text().strip().split('\n'))
                    f_out.write(str(a) + '\n')

    except Exception as e:
        print(e)

if __name__=='__main__':
    for url in all_url:
        fetch(url)