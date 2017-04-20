
from multiprocessing import Pool
import requests
from requests.exceptions import ConnectionError


def scrape(url):
    try:
        print (requests.get(url))
    except ConnectionError:
        print ('Error Occured ', url)
    finally:
        print ('URL ', url, ' Scraped')


if __name__ == '__main__':
    pool = Pool(processes=4)
    urls = [
        'https://www.baidu.com',
        'http://www.meituan.com/',
        'http://blog.csdn.net/',
        'http://xxxyxxx.net'
    ]
    pool.map(scrape, urls)