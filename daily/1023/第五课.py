# #python 第五课.py
# #复习
# num = [1,2,3,4,33,5,6,7,8,9]
# for n in num:
#     print(n)
#     if n == 33 :
#         break#退出循环
#     if n % 2 != 0:#奇数
#         print(f"跳奇数{n}")
#         continue#跳过后面的代码
#     print(f"跳偶数{n}")
#     print("你好")
# #字典 一一对应/一对多
# dic = {"num1":"12345678","nam":"jackie","age":"34"}
# print(dic["age"])#字典【索引，值】就是键

# #range自定义循环
# for i in range(1,5):#左闭右开
#     print(i)
# for i in range(5):
#     print("eeeee")

# #while循环，条件循环容易出现死循环
# while n <= 10 :
#     n += 1
#     print(n)

# #while True：(绝对死循环)





# #第五课
# #函数和打字小游戏
# def add(x,y):#加法
#     c=x+y
#     print(c)
#     return c
# c=add(1,2)

# def greet(name):#定义不是执行
#     print("你好"+name)

# greet(input("Please input the name:"))
# greet("jj")

# #无参函数
# def print_line():
#     print("_"*10)
# print_line()

# #多个参数调用要一一对应，参数名可以和外部的同名无影响
# #返回的值可以调用，多个返回的值用逗号隔开，调用也一样
# print(c)

# #打字小游戏
# import random
# import time

# words=["hallo","yellow","red","orange"]
# def choice_word(word_list):
#     words = random.choice(word_list)#调用words
#     return words
# def accuracy(target,user_input):
#     count = 0#正确数目
#     a=0
#     for i in range(len(user_input)):
#         a += 1
#         if user_input[i]==target[i]:
#             count +=1
#         return count/a
    
# print("-"*40)
# target = choice_word(words)
# print(f"目标单词{target}")

# start = time.time()
# mine=input("请输入：")
# end = time.time()
# spend =end-start
# rate=accuracy(target,mine)
# print(f"用时：{spend}")
# print(f"正确率：{rate*100}%")






#BACBD














