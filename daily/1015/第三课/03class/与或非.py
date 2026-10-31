#坐过山车例子：满足身高和有钱
height = 3
has_money = True
print(height > 1.4 and has_money)#and判断的条件是两个都为True，才会是True

#休息例子：只要是周末或者节假日就可以休息
is_weekend = True
is_holiday = False
print(is_weekend or is_holiday)#or判断条件是只要有一个条件满足，就是True

is_raining = False
print(not is_raining)#not就是把原本的bool类型颠倒过来