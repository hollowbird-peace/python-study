#别人写的，拿来把你

#import语句,以下是引入模块中函数的两种方法
import statistics#from statistics import median, mean

print(statistics.medisan([19,-5,36]))#print(median([19,-5,36]))
print(statistics.mean([19,-5,36]))#print(mean([19,-5,36]))

#还有第三种方式，会把模块中的所有内容进行引入(不推荐)
#from statistics import * 