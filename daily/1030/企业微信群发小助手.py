import pyautogui as pg
import pyperclip as pc
pg.PAUSE = 1

all_person = ['阳阳', '木星', '星烨']


def input_Chinese(word):# 打包一个可以输入中文到其他窗口的函数
    pc.copy(word)
    pg.hotkey("ctrl","v")

def opne_wx():
    pg.press("win")
    input_Chinese("企业微信")# 函数里面也是可以调用其他函数的
    pg.press("enter")
    pg.sleep(1)
    try:
        pg.locateOnScreen("wechat.png",confidence=0.9)
        print("打开成功")
    except pg.ImageNotFoundException:
        pg.alert("没有找到图片")
        exit()# 终止程序

def send_message(nickname,message):
    try:# 找搜索框中心点并点击
        x, y = pg.locateCenterOnScreen('pic.png', confidence=0.9)
        pg.click(x, y)
        input_Chinese(nickname) # 粘贴姓名
        pg.press('enter') # 进入聊天
        input_Chinese(message) # 粘贴消息
        pg.press('enter') # 发送
    except pg.ImageNotFoundException:
        pg.alert('没找到搜索框')

opne_wx()
#send_message("阳阳老师","你好")

try:
    for name in all_person:
        msg = f"{name}同学,你好"
        send_message(name,msg)
except pg.FailSafeException:
    pg.alert('紧急停止')
    exit()

pg.alert("发送结束")




# =====================================================================
# 【终极交付指南】如何将 Python 脚本打包成独立的 exe 文件
# =====================================================================
# 
# 一、 安装打包工具 (在 CMD 终端或 VS Code 终端执行)
# 1. 基础安装：
#    pip install auto-py-to-exe
# 2. 如果官方源下载太慢/报错，建议使用国内镜像源（如清华源）：
#    pip install auto-py-to-exe -i https://pypi.tuna.tsinghua.edu.cn/simple
# 
# 二、 启动工具
# 安装完成后，在终端输入以下命令，会自动弹出一个可视化的网页界面：
#    auto-py-to-exe
# 
# 三、 界面参数设置 (核心步骤)
# 1. Script Location (选脚本位置)：选择你的 .py 文件。
# 2. Onefile (打包方式)：选择 "Onefile" (打包成单个 exe 文件)。
# 3. Console (控制台窗口)：选择 "Window Based (hide the console)" 
#    (隐藏黑色的命令行窗口，适合纯图形界面或自动操作的小工具)。
# 4. Icon (图标)：可以选一个 .ico 格式的文件作为程序图标。
#    (注：如果只有 png 图片，可以在这个在线网站转换：https://ico.ideaseek.cn/)
# 5. 设置好输出路径（如桌面），点击底部的 "CONVERT" 开始打包。
# 
# =====================================================================
# ⚠️ 【最容易踩的坑（划重点）】
# =====================================================================
# 1. 资源文件丢失问题：
#    打包工具只会把 Python 解释器和代码塞进 exe 里。
#    如果你的代码里用到了外部图片（如 wechat.png, search.png, qq.png 等），
#    这些图片【绝对不会】自动被打包进去！
# 2. 解决方法：
#    必须手动将这些截图文件，跟生成的 .exe 文件【放在同一个文件夹内】。
#    如果缺失任何一张图片，程序运行到那里就会直接报错 "ImageNotFound"。
# =====================================================================

#BBCCB