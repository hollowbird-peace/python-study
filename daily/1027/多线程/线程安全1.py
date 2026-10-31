#python 线程安全1.py
#不安全演示
import threading
import time

count = 0

def add_count():
    global count#声明取用的是定义之外的count
    for i in range(100000):
        count += 1#最终count=100000

threads=[]
for _ in range(10):#10个线程
    t = threading.Thread(target=add_count)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
#无“锁”的多线程代码结果容易出错
print(f"最终结果{count}")