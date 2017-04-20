#coding:utf-8
import requests
from bs4 import  BeautifulSoup
import lxml
import time
all_link=[]
all_addr=[]
all_name=[]
def scrap(page):
    url='http://www.dianping.com/search/category/4/10/g113p{0}?aid=32501719%2C69310636%2C66250176%2C67087758%2C38080672%2C68919582%2C66710311%2C32526514%2C70733025%2C20246808%2C76837516&cpt=32501719%2C69310636%2C66250176%2C67087758%2C38080672%2C68919582%2C66710311%2C32526514%2C70733025%2C20246808%2C76837516&tc=1'.format(page)
    print (url)
    try:
        headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
        }
        web_data=requests.get(url,headers = headers)
        web_data.encoding='utf-8'
        content=web_data.text
        # print (content)
        soup = BeautifulSoup(content, 'lxml')
        # print (soup)
        addr = soup.find_all('span',class_='addr')
        shop_name=soup.find_all('h4')[3:]
        href=soup.find_all(name='div', attrs={"class":"pic"})
        for url ,adr,name in zip(href,addr,shop_name):
            link=url.find('a')
            # print (link)
            all_link.append(link)
            all_addr.append(adr.get_text())
            print (adr.get_text())
            all_name.append(name.get_text())
            print (name.get_text())
    except Exception as e:
        print(e)
def write_file():
    with open('dazhong.txt','a')as f:
        for a,b,c in zip(all_link,all_addr,all_name):
            f.write('http://www.dianping.com/'+a.get('href')+','+b+','+c+'\n')
if __name__=='__main__':
    for i in range(1,51):
        scrap(i)
        time.sleep(20)
    write_file()