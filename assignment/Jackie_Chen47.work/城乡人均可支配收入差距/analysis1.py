#python analysis1.py
#以下代码用于做出城乡收入与消费的绝对差距和相对差距
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
file_name = "all_data(已清洗).csv" 
df = pd.read_csv(file_name, encoding="utf-8-sig")
#只要“元”的数据
df_money0 = df[df['单位'] == '元']
#只要“收入”的数据
df_money1 = df_money0[df_money0['收支类型'] == '支出']
#筛选：不包含后面的细项和中位数
condition = df_money1['指标'].str.contains('人均消费支出') & ~df_money1['指标'].str.contains('经营|工资|财产|转移|中位数')
df_money2 = df_money1[condition]
print(f"2. 最终筛选出的核心行数: {len(df_money2)}")
#用数据透视表，把“范围”变成列名，把“数值”填进去
#行是年份，列是“全国”、“城镇”、“农村”
df_pivot = df_money2.pivot_table(index='年份', columns='范围', values='数值')

#计算绝对差距（城镇 - 农村）
df_pivot['收入绝对差'] = df_pivot['城镇'] - df_pivot['农村']

#计算相对差距（城镇 ÷ 农村）
df_pivot['收入倍数'] = df_pivot['城镇'] / df_pivot['农村']

print(df_pivot) #打印出来看一眼,没问题就开始作图


plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False    

#图3城乡收入绝对差距（柱状图）,X轴是年份，Y轴是刚刚算出的差值
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df_pivot.index, df_pivot['收入绝对差'], width=0.6, label='绝对差额')
ax.set_title("2019-2025年城乡人均可支配收入绝对差距", fontsize=16)
ax.set_xlabel("年份", fontsize=12)
ax.set_ylabel("差额 (元)", fontsize=12)
ax.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("2019-2025年城乡人均可支配收入绝对差距.png",dpi=300,bbox_inches='tight')
plt.show()

#图4城乡收入相对差距（折线图）
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df_pivot.index, df_pivot['收入倍数'], marker='s', linewidth=2, label='相对倍数')
ax.set_title("2019-2025年城乡人均可支配收入相对差距", fontsize=16)
ax.set_xlabel("年份", fontsize=12)
ax.set_ylabel("倍数 (倍)", fontsize=12)
plt.xticks(df_pivot.index) 
ax.legend()
plt.grid(linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("2016-2025年城乡人均可支配收入相对差距.png",dpi=300,bbox_inches='tight')
plt.show()
