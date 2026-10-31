#python lesson7.py
#写个小程序
import pyautogui as pg
import pyperclip as pc
import time
import sys

pg.PAUSE=1

person=["a","b","c"]
def input_chinese(word):
    pc.copy(word)
    pg.hotkey("ctrl","v")

def open_qq():#打开QQ
    pg.press("win")
    input_chinese("qq")
    pg.press("enter")
    time.sleep(1)
    # try:
    #     pg.locateOnScreen("qq.png",confidence=0.9)
    #     print("打开成功")
    # except pg.ImageNotFoundException:
    #     pg.alert("没找到图片")
    #     exit()

open_qq()
sys.exit()