#python 线程池.py
from concurrent.futures import ThreadPoolExecutor
import time

# 模拟一个耗时的任务，并返回结果
def download(file_id):
    time.sleep(1)  # 假装下载需要1秒
    return f"文件 {file_id} 下载完成"
# 【核心】创建一个最多容纳 3 个线程的线程池
with ThreadPoolExecutor(max_workers=3) as executor:
    # 准备5个任务（5个文件ID）
    file_ids = [1, 2, 3, 4, 5]
    
    # 【提交任务】把任务丢给线程池
    futures = []
    for file_id in file_ids:
        future = executor.submit(download, file_id)
        futures.append(future)
    
    # 【收集结果】等待所有任务完成并获取返回值
    for future in futures:
        print(future.result()) 

#=============================================================
with ThreadPoolExecutor(max_workers=3) as executor:
    file_ids = [1, 2, 3, 4, 5]
    
    # 【一行代码搞定】
    # 结果会按 file_ids 的顺序返回
    results = executor.map(download, file_ids)
    
    for res in results:
        print(res)
