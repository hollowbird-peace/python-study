#python analysis2.py
#以下代码用于做出2016 年与 2025 年四类收入来源占比图
import requests as req
import json
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import time
import pandas as pd
import matplotlib.pyplot as plt
import re
import csv

#读取数据
file_name="all_data(已清洗).csv" 
df = pd.read_csv(file_name, encoding="utf-8-sig")
#只要“元”的数据
df_money0=df[df['单位'] == '元']
#只要“收入”的数据
df_money1=df_money0[df_money0['收支类型'] == '收入']
df_money2=df_money0[df_money0['范围'] == '全国']
#筛选：不包含后面中位数
condition=df_money2['指标'].str.contains('经营|工资|财产|转移|中位数')& ~df_money2['指标'].str.contains('中位数')
df_money3=df_money2[condition]
china_2016=df_money3[df_money2['年份']=='2016年']
china_2025=df_money3[df_money2['年份']=='2025年']
print(f"2. 最终筛选出的核心行数: {len(df_money3)}")
print(f"2. 最终筛选出的核心行数: {len(china_2016)}")
print(f"2. 最终筛选出的核心行数: {len(china_2025)}")
#可以看到成功得到了四类数据，然后是作图

plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False  

#准备画图，画布设置大一点，因为要并排放两个饼图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
#画左边的饼2016年
labels_2016 = china_2016['指标'].str.replace('居民人均可支配', '').str.replace('（元）', '').str.replace(' ', '')#省略了一些无用的
sizes_2016 = china_2016['数值']
ax1.pie(sizes_2016, labels=labels_2016, autopct='%1.1f%%', startangle=90)#保留一位小数
ax1.set_title("2016年全国居民收入来源结构", fontsize=15)


#画右边的饼2025年
labels_2025 = china_2025['指标'].str.replace('居民人均可支配', '').str.replace('（元）', '').str.replace(' ', '')
sizes_2025 = china_2025['数值']
ax2.pie(sizes_2025, labels=labels_2025, autopct='%1.1f%%', startangle=90)
ax2.set_title("2025年全国居民收入来源结构", fontsize=15)
#保存
plt.savefig("2016年与2025年全国居民四类收入来源占比变化.png",dpi=300,bbox_inches='tight')

#整个大标题并展示
plt.suptitle("2016年与2025年全国居民四类收入来源占比变化", fontsize=18, y=0.98)
plt.tight_layout()
plt.show()
