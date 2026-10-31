#python analysis.py
#以下代码用于做出人均消费收入和支出俩张图
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
df_money1 = df_money0[df_money0['收支类型'] == '支出']

#筛选：不包含后面的细项和中位数
condition = df_money1['指标'].str.contains('人均消费支出') & ~df_money1['指标'].str.contains('经营|工资|财产|转移|中位数')
df_money2 = df_money1[condition]
print(f"2. 最终筛选出的核心行数: {len(df_money2)}")
#把“2025年”变成纯数字 2025，方便排序和画图
df_money2['年份_数字'] = df_money2['年份'].str.replace('年', '').astype(int)
#按年份从小到大排序（解决X轴反向问题）
df_money2 = df_money2.sort_values('年份_数字')

#解决中文字体乱码和负号显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False    


#开始作图
#创建画布（大画框 fig，画图纸 ax）
fig, ax = plt.subplots(figsize=(10, 6))

#用一个循环，画出三条线
for area in ['全国', '城镇', '农村']:
    #挑出当前区域的数据
    df_money3 = df_money2[df_money2['范围'] == area]
    
    #画线：X轴是年份，Y轴是数值，marker='o'画个圆点，label用来做图例
    ax.plot(df_money3['年份'], df_money3['数值'], marker='o', label=area, linewidth=2)

#设置标题和坐标轴标签
ax.set_title("2016-2025年全国、城镇和农村人均消费支出趋势", fontsize=16)
ax.set_xlabel("年份", fontsize=12)
ax.set_ylabel("金额 (元)", fontsize=12)

#显示图例
ax.legend(fontsize=12)

#添加网格线
ax.grid(True, linestyle='--', alpha=0.6)

#保存并展示图片
plt.savefig("全国、城镇和农村人均消费支出的年度变化.png",dpi=300,bbox_inches='tight')
plt.show()