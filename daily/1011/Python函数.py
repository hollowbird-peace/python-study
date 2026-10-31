#不做代码复读机

# sum函数对序列进行求和计算
#例:sum([1,-6,23,6,7])

#接下来是一些定义函数的代码，含参数的代码更具有通用性
#定义一个计算扇形面积的函数
def calculate_sector(central_angle,radius):#sector表示区域
    sector_area=central_angle/360*3.1415926*radius**2
    print(f"此扇形面积是:{sector_area}")
    return sector_area
#return函数可以返回函数值，获得能储存不同扇形面积的变量



calculate_sector(90,30)