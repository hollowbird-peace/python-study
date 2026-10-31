#python 第六课.py
import pyautogui as pg
import os
import time
# print(pg.position())#确定鼠标位置
#全局延时一秒:所有的操作都延时一秒
'''
pg.PAUSE=1#pg.sleep==time.sleep
'''
# for i in range(10,0,-1):
#     time.sleep(1)
#     print(i)
print("开始确定鼠标位置")
time.sleep(1)
while True:#Ctrl+C终止程序
    x,y=pg.position()
    print(pg.size)#查看电脑分辨率
    print(x,y)
    os.system("cls")#清屏
#BCDAC