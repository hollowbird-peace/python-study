import requests as req
import json
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import time
import pandas as pd
import matplotlib.pyplot as plt
import re
import csv

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "priority": "u=0, i",
    "referer": "https://movie.douban.com/top250?start=50&filter=",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"141\", \"Google Chrome\";v=\"141\", \"SLBrowser\";v=\"9\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36"
}

cookies = {
    "bid": "d4DTubVc0To",
    "_pk_id.100001.4cf6": "7cd2a78b67b0b12a.1787727068.",
    "ll": "\"118215\"",
    "_ga": "GA1.1.775976324.1791443827",
    "_ga_Y4GN1R87RG": "GS2.1.s1791522785$o4$g0$t1791522826$j19$l0$h0",
    "_pk_ref.100001.4cf6": "%5B%22%22%2C%22%22%2C1791552052%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DarawjxqxjMKdFiURqymt1EEkp3...",
    "_pk_ses.100001.4cf6": "1",
    "_utma": "223695111.479755692.1787727068.1791522831.1791552052.8",
    "_utmb": "223695111.0.10.1791552052",
    "_utmc": "223695111",
    "_utmz": "223695111.1791552052.8.8.utmcsr=baidu|utmccn=(organic)|utmcmd=organic",
    "ap_v": "0,6.0"
}

base_url = 'https://movie.douban.com/top250'
params = {
    "start": "75",
    "filter": ""
}

with open("douban_movie1.csv", "w", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["电影名", "评分", "导演", "年份", "人评价"])
    writer.writeheader()
    for start in range(0, 250, 25):
        url = f"{base_url}?start={start}"
        res = req.get(url, headers=headers, cookies=cookies)
        html = res.text
        soup = BeautifulSoup(html, "html.parser")
        movie_list = soup.find_all("div", class_="item")
        print(f"本页数目:{len(movie_list)}")
        movie_list = soup.find_all("div", class_="item")
        print(f"====第{start//25 + 1}页，本页数目:{len(movie_list)}====")
        # 遍历本页所有电影
        for movie in movie_list:
            # 电影名称
            title = movie.find("span", class_="title").get_text(strip=True)
            # 评分
            rating = movie.find("span", class_="rating_num").get_text(strip=True)

            # 获取导演、年份所在文本
            info_text = movie.find("div", class_="bd").p.get_text()
            # 提取导演
            director = ""
            if "导演:" in info_text:
                dir_str = info_text.split("导演:")[1]
                if "主演:" in dir_str:
                    director = dir_str.split("主演:")[0].strip()
                else:
                    director = dir_str.strip()
            
            # 正则提取4位年份数字
            year_search = re.search(r'(\d{4})', info_text)
            year = year_search.group(1) if year_search else ""

            # 评价人数
            rating_span = movie.find("span", class_="rating_num")
            comment_num = ""
            if rating_span:
                span_list = rating_span.find_next_siblings("span")
                if len(span_list) >= 2:
                    comment_span = span_list[1]
                    comment_num = comment_span.get_text(strip=True)
                    comment_num = comment_num.replace("人评价", "")

            movie_data = {
                "电影名": title,
                "评分": rating,
                "导演": director,
                "年份": year,
                "人评价": comment_num
            }
            writer.writerow(movie_data)
            time.sleep(1)

print("成功")
# 数据清洗