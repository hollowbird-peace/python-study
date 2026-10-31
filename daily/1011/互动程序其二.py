"""
BMI计算公式:BMI = 体重 / (身高 ** 2)

BMI分类
偏瘦: BMI <= 18.5
正常: 18.5 < BMI <= 25
偏胖: 25 < BMI <= 30
肥胖: 30 < BMI

写一个计算BMI的函数,函数名为calculate_BMI.
1.可以计算任意体重和身高的BMI值
2.执行过程中打印一句话，"您的BMI分类为:xx'
3。返回计算出的BMI值
"""
def calculate_BMI(weight,height):
    try:
        if weight>=0 and height>=0:
            print("你的体重(单位:kg):",weight)
            print("你的身高(单位:m):",height)
            BMI=weight/(height**2)
            print(BMI)
            if BMI<= 18.5:
                print("偏瘦")
            elif 18.5 < BMI <= 25:
                print("正常")
            elif 25 < BMI <= 30:
                print("偏胖")
            else :
                print("肥胖")
            return BMI
        else:
            print("身高和体重值不能为负")
    except ValueError:
        print("格式非法")
####################################################

result=calculate_BMI(60,1.6)
