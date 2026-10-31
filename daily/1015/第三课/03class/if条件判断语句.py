score = 55
#if else只会执行其中一个
if score >= 60 :#必须加冒号
    print("不会挂科")#:后面的内容必须缩进，就是提醒各位，这一行代码附属于上一行
else :#上面if条件不满足的其他情况就是else
    print("挂科啦")

num = 660
if num >=580 :
    print("恭喜你，考上了一本")
elif num>=530 :
    print("恭喜你,考上了二本")
elif num>=300 :
    print("恭喜你考上了专科")
else :#else一定要写在最后，代表排除上面索引情况
    print("请考虑复读")