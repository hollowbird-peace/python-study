#python 线程安全2.py
#安全演示
import threading
count=0
#创建一把锁
lock=threading.Lock()

def add_count():
    global count
    for i in range(100000):
        with lock:#加锁：无法被打断
            count += 1#结束，自动开锁

threads=[]
for _ in range(10):
    t = threading.Thread(target=add_count)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"最终结果{count}")