#python 多线程程序.py
import threading
import time
from concurrent.futures import ThreadPoolExecutor,as_completed
import random
import logging

#设置日志格式：时间-名称-线程名-消息
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%H:%M:%S")
bad =0
good = 0

def download(file_id):
    start_time=time.time()
    max_attempts=3
    for n in range(max_attempts):
        try:
            time.sleep(random.random())
            if random.random()<0.6:
                raise ConnectionError("模拟网络断开")
            else:

                return True,f"文件{file_id}成功,耗时{time.time()-start_time}"
        except ConnectionError:
            time.sleep(0.1*2**n)
            if n==2:
                return False,f"文件{file_id}失败,耗时{time.time()-start_time}"

file_ids=[]
for i in range(1,21):
    file_ids.append(i)

start_time=time.time()

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = []
    for file_id in file_ids:
        future = executor.submit(download, file_id)
        futures.append(future)

    for future in as_completed(futures):
        try:
            a, b = future.result(timeout=5)
            logging.info(f"任务结果：{b}")
            if a==True:
                good+=1
            else:
                bad+=1
        except Exception as e:
            logging.info(f"任务异常:{e}"); bad += 1; continue

end_time=time.time()

ti = end_time-start_time

logging.info(f"任务用时{ti}秒，主线程全部结束，失败{bad},成功{good}")