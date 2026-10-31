import urllib.request
from urllib.request import Request, urlopen
import time
import os
import random
import ssl

START_CHAPTER = 1      # 起始章节
END_CHAPTER = 5      # 结束章节
BASE_URL = "https://www.bqg371.cc/#/book/1499/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ..."}
save_folder = 'bqg371_新小说名'#<要改>
if not os.path.exists(save_folder):
    os.makedirs(save_folder)
url_list = []
for i in range(START_CHAPTER, END_CHAPTER + 1):
    # ⚠️ 根据新网站的真实链接规律来拼接<要改>
    # 如果链接是 /read/1499/1.html，就用下面这行：
    url_list.append(f"{BASE_URL}{i}.html") 
    # 如果新网站有第二页的（比如 1_2.html）
    # url_list.append(f"{BASE_URL}{i}_2.html") 
print(f"总共生成了 {len(url_list)} 个待下载任务，准备开始...\n")
context = ssl._create_unverified_context() # 忽略 SSL 证书错误
success_count = 0
fail_count = 0
for index, url in enumerate(url_list):
    filename = url.split('/')[-1]
    # 【断点防封】如果文件已经存在，就跳过，避免重复下载和被封 IP
    filepath = os.path.join(save_folder, filename)
    if os.path.exists(filepath):
        print(f"⏭️ 跳过已存在: {filename}")
        continue

    try:
        req = Request(url, headers=headers)
        resp = urlopen(req, context=context)
        
        # 读取并解码
        html_content = resp.read().decode('utf-8', errors='ignore')
        
        # 保存到文件
        with open(filepath, mode='w', encoding='utf-8') as f:
            f.write(html_content)
            
        success_count += 1
        # 【进度条】
        print(f"✅ [{index + 1}/{len(url_list)}] 下载成功: {filename}")
        
        # 【防封】随机休息 1 到 3 秒，模拟真人阅读速度
        time.sleep(random.uniform(1, 3))
        
    except Exception as e:
        fail_count += 1
        print(f"❌ [{index + 1}/{len(url_list)}] 抓取失败: {url} | 错误: {e}")
        # 如果遇到报错，多休息一会儿，防止被彻底拉黑
        time.sleep(5)

print("\n" + "="*40)
print(f"🎉 批量下载完成！成功: {success_count} 个，失败: {fail_count} 个。")
print("over!")