import re
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("douban_movie1.csv", encoding="utf-8-sig")
print("----原始数据----")
print(df.info())  # df就是pandas的DataFrame .info()拆看表格的信息
print("原始数据:", len(df))

# 去除字段首尾
df["电影名"] = df["电影名"].str.strip()
df["导演"] = df["导演"].astype(str).str.strip()
df["导演"] = df["导演"].str.replace("\n", "").str.strip()
df["导演"] = df["导演"].str.replace(r"\s", "", regex=True)
df["年份"] = df["年份"].astype(str).str.strip()

# 处理空值
df = df.dropna(subset=["电影名"])
df["导演"] = df["导演"].fillna("未知")
df["年份"] = df["年份"].fillna("未知")
df["评分"] = df["评分"].fillna(0)
df["人评价"] = df["人评价"].fillna(0)

# 去重
df = df.drop_duplicates(subset=["电影名"], keep="first")
print("去重后行数:", len(df))

# 类型转换
df["评分"] = pd.to_numeric(df["评分"], errors="coerce")
df["人评价"] = pd.to_numeric(df["人评价"], errors="coerce").fillna(0).astype(int)

def clean_year(y):
    res = re.search(r"\d{4}", str(y))
    if res:
        return res.group()
    else:
        return "未知"

df["年份"] = df["年份"].apply(clean_year)
df.to_csv("douban_movie_clean1.csv", index=False, encoding="utf-8-sig")
print("清洗完成,保存在douban_movie_clean.csv")
print("----清洗预览----")
print(df.head())

# 数据处理可视化
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams["axes.unicode_minus"] = False

# 评分直方图
plt.figure(figsize=(8, 5))
plt.hist(df["评分"], bins=15, color="#2f70b1")  # hist直方图
plt.title("电影评分分布直方图")
plt.xlabel("评分")
plt.ylabel("电影数量")
plt.savefig("评分分布.png")
plt.show()

# 年份-评分散点图
df_year = df[df["年份"] != "未知"].copy()
df_year["年份数字"] = df_year["年份"].astype(int)
plt.figure(figsize=(10, 5))
plt.scatter(df_year["年份数字"], df_year["评分"], alpha=0.6)  # scatter散点图
plt.title("年份-评分散点图")
plt.xlabel("年份")
plt.ylabel("评分")
plt.savefig("年份平分散点.png")
plt.show()

# 导演前10柱状图
top_people = df["导演"].value_counts().head(10)
plt.figure(figsize=(10, 5))
top_people.plot(kind="bar")  # 绘制柱状图
plt.title("导演前10的作品")
plt.xlabel("导演")
plt.ylabel("作品数量")
plt.xticks(rotation=45)  # 导演名字旋转45度防止名字挤在一起
plt.tight_layout()  # 自动调整布局防止名字被截
plt.savefig("导演前10.png")
plt.show()