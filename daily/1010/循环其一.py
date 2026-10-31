#for 变量名 in 可迭代对象:(对每个变量做一些事情)
#dict.keys表示所有键
#dict.values表示所有值
#dict.items表示所有键值对
#例子:班级中同学的体温
classmate_tem={"小明":36.5,"小王":38.2,"小张":37.2,"小李":36.9,"小美":37.7}
for classmate,tem in classmate_tem.items():
    if tem>=37.5:
        print(classmate,tem)
    
#renge(5,10,2)表示赋值从5到9,步长为2
#例:从1加到100
a=0
for i in range(1,101):
    a=a+i
print(a)