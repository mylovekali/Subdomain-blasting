import requests
import time
import queue
from lxml import etree

def baidu_get():
    while not q.empty():
        url = q.get()
        rep = requests.get(url, header=headers)
        time.sleep(0.5)
        baidu = rep.text
        code = etree.HTML(baidu)
        codes = code.xpath('//div[@class="f13"]')
        for codess in codes:
            codesss = codess.xpath(',/a[1]')
            for codessss in codesss:
                codesssss = codessss.xpath('@href')
                bd_url = codesssss[0]
                bd_rep = requests.get(bd_url)
                print(bd_rep.url)

if __name__ == '__main__':
    q=queue.Queue()
    url='https://www.baidu.com/s?wd=inurl:sohu.com&pn=0'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
    }

    for i in range(100):
        i=i*10
        urls=url+str(i)
        q.put(urls)

    baidu_get()





























