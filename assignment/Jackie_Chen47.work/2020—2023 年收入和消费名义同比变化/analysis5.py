#python analysis5.py
#以下代码用于做出2020—2023 年收入和消费名义同比变化图
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

df_money=df[(df['范围'] == '全国') & (df['单位'] == '元')&\
            df['指标'].str.contains('人均可支配收入|人均消费支出')&\
            ~df['指标'].str.contains('中位数|工资|经营|财产|转移|食品|衣着|居住')]
df_money['指标'] = df_money['指标'].str.replace(r'.*居民人均', '', regex=True)
df_money1 = df_money.pivot_table(index='年份', columns='指标', values='数值', aggfunc='sum')

df_money1['收入同比增速(%)'] = df_money1['可支配收入 '].pct_change() * 100
df_money1['支出同比增速(%)'] = df_money1['消费支出 '].pct_change() * 100
# 把索引里的“年”字去掉，并转换成整数类型（int）
df_money1.index = df_money1.index.str.replace('年', '').astype(int)
#截取2020-2023这一段，用于画图
df_money1 = df_money1.loc[2020:2023]

plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False    

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(df_money1['收入同比增速(%)'], marker='o', label='收入增速', linewidth=2)
ax.plot(df_money1['支出同比增速(%)'], marker='o', label='支出增速', linewidth=2)

ax.set_title("2016-2025全国八类消费支出结构变化图", fontsize=16)
ax.set_xlabel("年份", fontsize=12)
ax.set_ylabel("同比增速(%)", fontsize=12)
ax.legend(title='消费类别', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.xticks(df_money1.index)#让x轴数字变成整数
plt.tight_layout()
#添加网格线
ax.grid(True, linestyle='--', alpha=0.6)
plt.savefig("2020—2023 年收入和消费名义同比变化",dpi=300,bbox_inches='tight')
plt.show()