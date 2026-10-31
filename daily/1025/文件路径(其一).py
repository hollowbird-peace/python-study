#python 文件路径(其一).py
#让代码知道文件的位置
#绝对路径和相对路径

#操作：打开文件并读取

#r是读取，不写默认也是读取文件，然后encoding是可选参数表示编码方式
f=open("D:\work\python\student\daily\\1025\文件.txt","r",encoding="utf-8")#路径含数字要加转义符“\”
print(f.read(5))#有的文件比较大，read(5)表示读5个字节
print(f.read(1))#下一次调用会继续往下读
print(f.readline())#只读一行，重复读下一行
line = f.readline()
while line !="":#一直读直到读空停下
    print(line)
    line = f.readline()
#或者用readlines函数也可以读取全部内容
f.close()#关闭文件，释放资源

#或者用with ... as ...可以在运行结束之后自动关闭文件
'''
with open("D:\work\python\student\daily\\1025\文件.txt") as f:
    print(f.read())#操作
'''
