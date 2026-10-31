#python 会用.py
import threading
import time

def worker(name):
    print(f"[{name}]开始")
    time.sleep(2)
    print(f"[{name}]结束")

t1 = threading.Thread(target=worker,args=("任务A",))
t2 = threading.Thread(target=worker,args=("任务B",))

#添加此代码，变成守护线程
#没有join，会在主线程结束后关闭线程，来不及输出结束
#t1.daemon=True
#t2.daemon=True

t1.start()
t2.start()

t1.join()
t2.join()

print("主线程全部结束")