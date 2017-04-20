#coding:utf-8
import requests
from bs4 import  BeautifulSoup
from multiprocessing import Pool
import lxml,time
all_url=[]
all_phone=[]
all_shop_name=[]
# with open('dazhong.txt','r')as f:
#     for i in f:
#         url=i.split(',')[0]
#         all_url.append(url)
url='http://www.dianping.com//shop/79310987'
# def get_phone(url):
try:
    print (url)
    headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    web_data=requests.get(url,headers = headers)
    web_data.encoding='utf-8'
    content=web_data.text
    soup = BeautifulSoup(content, 'lxml')
    # print (soup)
    can = soup.select('p[class="expand-info tel"]')
    shop_name=soup.select('h1[class="shop-name"]')
    # shop_name=soup.find_all('span',class_='item')
    # can =soup.find_all('span',class_='geo')
    # can =soup.find('p',class_="expand-info tel")
    # print (can)
    # print (shop_name)
    for i ,j in zip(can,shop_name):
        print (j.get_text()[:-5].strip())
        all_shop_name.append(j.get_text()[:-5].strip())
        all_phone.append(i.get_text().strip().split('\n'))

except Exception as e:
    print(e)
# def write_file():
with open('dazhong_phone_new.txt','a')as f_out:
    for sp_name,phone in zip(all_shop_name,all_phone):
        f_out.write(str(sp_name+','+str(phone)+'\n'))
# if __name__=='__main__':
#     pool = Pool(processes=4)
#     pool.map(get_phone, all_url)
#     write_file()