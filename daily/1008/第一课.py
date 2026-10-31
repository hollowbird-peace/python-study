#打印hello world，在代码中可以加空格
print(    "hello world"   )
"""
运行：右上三角形/快捷键Ctrl+F5
字体调节:代码区左下齿轮设置、终端区Ctrl+,
颜色调节:左下齿轮设置搜索color
排查bug:在代码前面写井号
"""
#缩进用tab键，但代码前不能随意缩进！
#代码是从上到下进行的！

import pyttsx3
engine = pyttsx3.init()
#要朗读的文字
text="快来看看啊！！！"
engine.say(text)
engine.runAndWait()