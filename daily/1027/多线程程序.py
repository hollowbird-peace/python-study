#python 多线程程序.py
import threading
import time
import requests as req
import urllib3
from concurrent.futures import ThreadPoolExecutor
#关闭因为忽略真书而产生的红色警告
urllib3.disable_warnings()

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0",
           "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Content-Type": "application/json",}

urls = [
    "https://baike.baidu.com/item/Python",
    "https://baike.baidu.com/item/人工智能",
    "https://baike.baidu.com/item/计算机科学",
    "https://baike.baidu.com/item/算法",
    "https://baike.baidu.com/item/数据结构"
]
more_urls=urls*10
def cah(url):
    try:
        res = req.get(url,headers=headers,timeout=5,verify=False)
        return f"成功{url}"
    except Exception as e:
         print(f"抓取失败,错误{e}")

sta=time.time()

for res in more_urls:
    cah(res)
    
end=time.time()
print(end-sta)


