#python analysis3.py
#以下代码用于做出全国八类消费支出结构变化图
import requests as req
import json
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import time
import pandas as pd
import matplotlib.pyplot as plt
import re
import csv


file_name="all_data(已清洗).csv" 
df=pd.read_csv(file_name, encoding="utf-8-sig")

#筛选只要“全国”，只要“元”，只要“支出”，还要的是具体的消费大类（食品、衣着等），排除“总消费支出”和“增长率”
df_money=df[(df['范围'] == '全国') & (df['单位'] == '元') & (df['收支类型'] == '支出')]
df_money1=df_money[df_money['指标'].str.contains('食品烟酒|衣着|居住|生活用品|交通通信|教育文化|医疗保健|其他用品')].copy()

#清理名字
df_money1['指标']=df_money1['指标'].str.replace('全国居民人均', '', regex=False).str.replace('支出', '', regex=False)

print(f"筛选出的消费类数据行数: {len(df_money1)}")
df_pivot = df_money1.pivot_table(index='年份', columns='指标', values='数值',aggfunc='sum')#aggfunc='sum'能防止同年有重复数据导致报错
df_pivot=df_pivot.sort_index()#让数据从大到小排列
#准备好了



plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False    

#开始画图：堆叠柱状图
fig, ax = plt.subplots(figsize=(12, 6))
#指定画堆叠柱状图(stacked=True)，并画在 ax 画纸上
df_pivot.plot(kind='bar', stacked=True, ax=ax, width=0.7)
ax.set_title("2016-2025全国八类消费支出结构变化图", fontsize=16)
ax.set_xlabel("年份", fontsize=12)
ax.set_ylabel("消费金额(元)", fontsize=12)
ax.legend(title='消费类别', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.xticks(rotation=0)#让X轴上数字横过来
plt.tight_layout()
plt.savefig("2016-2025全国八类消费支出结构变化图.png",dpi=300,bbox_inches='tight')
plt.show()
