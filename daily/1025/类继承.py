#python 类继承.py
#子类与父类，优先看所属的类有没有该方法，无则取父类的方法


# 类继承练习：人力系统

# · 员工分为两类：全职员工 FullTimeEmployee、兼职员工 PartTimeEmployee。
# · 全职和兼职都有"姓名 name"、"工号 id"属性，
#   都具备"打印信息 print_info"（打印姓名、工号）方法。
# · 全职有"月薪 monthly_salary"属性，
#   兼职有"日薪 daily_salary"属性、"每月工作天数 work_days"的属性。
# · 全职和兼职都有"计算月薪 calculate_monthly_pay"的方法，但具体计算过程不一样。

class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def print_info(self):
        print(f"名字是:{self.name}\n工号是:{self.id}")

class FullTimeEmployee(employee):
    def __init__(self,name,id,monthly_salary):
        super().__init__(name,id)
        self.monthly_salary=monthly_salary
    def calculate_monthly_pay(self):
        pay=self.monthly_salary
        print(f"月薪为{pay}" )

class PartTimeEmployee(employee):
    def __init__(self,name,id,daily_salary,work_days):
        super().__init__(name,id)
        self.daily_salary=daily_salary
        self.work_days=work_days
    def calculate_monthly_pay(self):
        pay=self.daily_salary*self.work_days
        print(f"月薪为{pay}" )



a =PartTimeEmployee("小明",10086,200,15)
b =a.print_info()
c =a.calculate_monthly_pay()












































































# class mammal:
#     def __init__(self,name,sex):
#         self.name=name
#         self.sex=sex
#     def breathe(self):
#         print(self.name +"在呼吸...")
#     def poop(self):
#         print(self.name +"在拉屎...")

# class human(mammal):
#     def __init__(self,name,sex):
#         super().__init__(name,sex)
#         self.has_tail=False
#     def poop(self):
#         print(self.name +"厕所在拉屎...")
#     def do(self):
#         print(self.name +"在阅读")

# class cat(mammal):
#     def __init__(self,name,sex):
#         super().__init__(name,sex)
#         self.has_tail=True
#     def do(self):
#         print (self.name +"在舔毛")
