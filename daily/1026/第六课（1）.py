#python 第六课（1）.py
import pyautogui as pg
import os
import time
#全局延时一秒:所有的操作都延时一秒,不叠加
pg.PAUSE=1#pg.sleep==time.sleep
#hotkey是快捷键
pg.hotkey("win","d")#win+d是切换界页面
pg.hotkey("win","d")

#moveTo是绝对移动|movePel是相对移动|duration指花费多少时间(不加是瞬移，可能报错)
pg.moveTo(1000,500,duration=1)
x,y=pg.size()
pg.moveTo(x/2,y/2,duration=1)

pg.moveRel(-100,100,duration=1)
pg.doubleClick()#双击
pg.click()#单击
pg.tripleClick()#三击
pg.rightClick(x/2,y/2,duration=1)#右键
pg.scroll(-500)#滚动：负数向下滚（不能加duration）
#dragTo绝对拖拽|dragRel相对拖拽
pg.dragTo(x/2,y/2,duration=1)
pg.hotkey("win","d")
pg.typewrite("cmd",interval=0.2)#interval是每个字符输入的间隔


import pyautogui as pg
pg.PAUSE = 1

# 按一下回车
pg.press("enter")

# 其他常用键名
pg.press("space") # 空格
pg.press("backspace") # 退格
pg.press("tab") # 制表符
pg.press("esc") # 退出
pg.press("volumeup") # 音量加
pg.press("volumemute") # 静音

import pyautogui as pg
import pyperclip as pc

# 1. 把中文先复制到系统剪贴板
pc.copy("你好，世界")

# 2. 再 Ctrl+V 粘贴到输入框
pg.hotkey("ctrl", "v")








