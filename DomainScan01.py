import sys
import os
import dns.resolver
import threading
import queue
import time

q=queue.Queue()

def domainscan():
    while not q.empty():
        domain=q.get()
        domain=domain+'.'+url
        domain=domain.replace('\n','')
        try:
            A = dns.resolver.query(domain,'A')
            for i in A.response.answer:
                print(i)
        except dns.exception.Timeout:
            print("解析延时，重试中---")
            time.sleep(0.1)
        except dns.resolver.NoAnswer:
            print("出现异常，重试中---")
            time.sleep(0.1)

def show():
    print('ps:scan.py baidu.com dir.txt 10')
    print('\n')
    print('脚本名 网站地址 字典文件 线程数')

if __name__ == '__main__':
    path=os.path.dirname(os.path.realpath(__file__))
    if len(sys.argv)<4:
        show()
        sys.exit()
    url=sys.argv[1]
    file=sys.argv[2]
    num=sys.argv[3]
    for dir in open(path+'/'+file):
        q.put(dir)
    for i in range(int(num)):
        t=threading.Thread(target=domainscan)
        t.start()

# cmd命令行下 C:\Users\XIAODI-PC>D:\python3\python.exe E:\myproject\DomainScan.py baidu.com dir.txt 15