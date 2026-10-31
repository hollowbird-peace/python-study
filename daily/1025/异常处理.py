#python 异常处理.py
#异常类型
#1
try:
    number_list =[1,2,3,4]
    number_list[4]#IndexError索引错误
except Exception as e:#别滥用吞bug!!!
    print(f"{e}")
#2
try:
    print(1/0)#ZeroDivisionError除零
except Exception as e:
    print(f"{e}")
#3
try:
    f=open(".\hallo.txt","r")#FileNotFoundError找不到文件错误/OSError路径不存在
except Exception as e:
    print(f"{e}")
#4
try:
    print("hallo"*"world")#TypeError类型错误
except Exception as e:
    print(f"{e}")
#5
try:
    int("10.5")#ValueError值错误
except Exception as e:
    print(f"{e}")


