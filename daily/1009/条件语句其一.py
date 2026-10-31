mood_index = int(input("对象今天的心情指数是(1~100):"))  # int函数将字符串转化为数字

if not (1 <= mood_index <= 100):
    print("格式非法")
elif mood_index >= 60:
    print("你可以玩一整天，爽去吧！！")
else:
    at_home = input("对象在家吗(输入在或不在):")
    if at_home == "不在":
        print("你可以玩一整天，爽去吧！！")
    elif at_home == "在":
        if mood_index >= 40:
            print("玩的时候小心点")
        else:
            print("你完蛋了")
    else:
        print("格式非法")
