#python 多线练习.py
import threading
import random
import queue

lock = threading.Lock()
sum =0
count = {}
q = queue.Queue(maxsize=10)

def producer(name):
    print(f"[{name}]开始")
    for i in range(100):
        num = random.randint(1,100)
        q.put((name,num))
        print(f"{name}生产了{num}")
    print(f"[{name}]结束")

def consumer(name):
    global sum
    count[name] = 0
    print(f"[{name}]开始")
    while True:
        item = q.get()
        try:
            if item is None:
                break
            real_name,real_num=item
            print(f"{name}消费了{real_name}生产的{real_num}")
            with lock:
                sum += real_num
                count[name] += 1
        except Exception as e:
            print(f"出现错误:{e}")
        finally:
            q.task_done()
    print(f"[{name}]结束")
    
producers=[]
for i in range(3):
    t1 = threading.Thread(target=producer,args=(f"生产任务{i}",))
    t1.start()
    producers.append(t1)

consumers=[]
for i in range(2):
    t2 = threading.Thread(target=consumer,args=(f"消费任务{i}",))
    t2.start()
    consumers.append(t2)

for i in producers:
    i.join()

for i in range(2):
    q.put(None)

q.join()

for i in consumers:
    i.join()

print("主线程全部结束")
print(f"总和：{sum},处理量：{count}")