#python 第七课.py
import pyautogui as pg
import pyperclip as pc
import time
pg.hotkey("ctrl","shift","esc")#hotkey按多个键#打开任务管理器
time.sleep(2)
pg.press("win")#press按单个键（回车，空格）,且不能用来打字
pg.press("shift")
pg.typewrite("hello world")#打一串字符，不支持中文
pc.copy("你好，世界")
pg.hotkey("ctrl","v")

pg.alert("HHHHHHHH")#弹出小窗口，更加直观#适合和异常出现代码一起写
exit()#终止程序：比如发生错误，不得不终止或没必要继续运行下去



