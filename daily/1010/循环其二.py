#for循环有明确的循环次数
#while循环无明确的循环次数，容易陷入死循环
#if 判断的是「值满不满足条件」
#try的是「这行代码能不能成功执行」
#try失败：跳过 try 里后面的语句，进入 except ValueError

#写一个对用户输入数字求平均值的计算机，要求：
#1.用户可以输入任意数量的数字
#2.最后输入q,表示所有数字输入完成
#3.程序给出平均值计算结果
#4.用户输入非数字时报错，并重新输入

all_num = []
print("您可以输入任意数字(不限数量和范围),输入q表示结束,然后该计算机进行求平均值。")

while True:
    user_num = input("请输入数字或q:")
    if user_num == "q":
        print("数字输入结束，开始计算")
        break
    try:
        all_num.append(float(user_num))  # 能转成数字才放进列表
        print(all_num)
    except ValueError:
        print("格式非法，请输入数字或q")

if len(all_num) == 0:
    print("没有输入数字，无法计算平均值")
else:
    c = 0
    b = len(all_num)
    for a in range(b):
        c = c + all_num[a]
    print("总和为", c, "平均值为", c / b)
