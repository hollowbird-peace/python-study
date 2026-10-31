#python analysis4.py
#以下代码用于做出最新年度城镇与农村消费结构对比图
import requests as req
import json
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import time
import pandas as pd
import matplotlib.pyplot as plt
import re
import csv

file_name = "all_data(已清洗).csv" 
df = pd.read_csv(file_name, encoding="utf-8-sig")

df_money0 = df[df['单位'] == '元']
df_money1 = df_money0[df_money0['收支类型'] == '支出']
df_money2 = df_money1[df_money1['年份'] == '2025年']
condition = df_money2['指标'].str.contains('食品烟酒|衣着|居住|生活用品|交通通信|教育文化|医疗保健|其他用品')
df_money3 = df_money2[condition]
# 把名字清理一下，把xx居民人均全用空白替换
df_money3['指标'] = df_money3['指标'].str.replace(r'.*居民人均', '', regex=True).str.replace('支出', '', regex=False)
# 透视表：行是城镇/农村，列是8个指标
df_money4 = df_money3.pivot_table(index='范围', columns='指标', values='数值', aggfunc='sum')


plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False    

fig, ax = plt.subplots(figsize=(12, 6))
#指定画堆叠柱状图(stacked=True)，并画在 ax 画纸上
df_money4.plot(kind='bar', stacked=True, ax=ax, width=0.7)
ax.set_title("2016-2025全国八类消费支出结构变化图", fontsize=16)
ax.set_xlabel("地区", fontsize=12)
ax.set_ylabel("消费金额(元)", fontsize=12)
ax.legend(title='消费类别', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.xticks(rotation=0)#让X轴上的字横过来
plt.tight_layout()
plt.savefig("2025年城镇与农村消费结构对比图.png",dpi=300,bbox_inches='tight')
plt.show()