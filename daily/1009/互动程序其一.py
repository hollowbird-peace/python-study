#BMI = 体重 / （身高 ** 2）
user_weight= float(input("请输入你的体重(单位:kg):"))
user_hight= float(input("请输入你的身高(单位:m):"))
user_BMI=user_weight/(user_hight)**2
print("您的BMI值是"+str(user_BMI))