import urllib.request
from urllib.request import Request, urlopen
import time
import os
import random
import ssl

# ==================== 1. 配置区域 ====================
# 【重要】请把这里改成你真实要下载的章节范围
START_CHAPTER = 1      # 起始章节
END_CHAPTER = 51     # 结束章节
BASE_URL = "https://www.biqubee.com/bi_7280/"  # 小说目录前缀

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}

# 创建保存文件夹
save_folder = 'biqubee_novel_all'
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# ==================== 2. 生成下载列表 ====================
url_list = []
for i in range(START_CHAPTER, END_CHAPTER + 1):
    url_list.append(f"{BASE_URL}{i}.html")
    url_list.append(f"{BASE_URL}{i}_2.html")
    # 如果你的网址有 1_3.html，可以继续加 url_list.append(f"{BASE_URL}{i}_3.html")

print(f"总共生成了 {len(url_list)} 个待下载任务，准备开始...\n")

# ==================== 3. 开始批量下载 ====================
context = ssl._create_unverified_context() # 忽略 SSL 证书错误
success_count = 0
fail_count = 0

for index, url in enumerate(url_list):
    # 提取文件名（比如从 .../1.html 提取出 "1.html"）
    filename = url.split('/')[-1]
    
    # 【断点防封】如果文件已经存在，就跳过，避免重复下载和被封 IP
    filepath = os.path.join(save_folder, filename)
    if os.path.exists(filepath):
        print(f"⏭️ 跳过已存在: {filename}")
        continue

    try:
        # 发送请求
        req = Request(url, headers=headers)
        resp = urlopen(req, context=context)
        
        # 读取并解码
        html_content = resp.read().decode('utf-8', errors='ignore')
        
        # 保存到文件
        with open(filepath, mode='w', encoding='utf-8') as f:
            f.write(html_content)
            
        success_count += 1
        # 【进度条】直观地看看到底下了多少
        print(f"✅ [{index + 1}/{len(url_list)}] 下载成功: {filename}")
        
        # 【防封核心】随机休息 1 到 3 秒，模拟真人阅读速度
        time.sleep(random.uniform(1, 3))
        
    except Exception as e:
        fail_count += 1
        print(f"❌ [{index + 1}/{len(url_list)}] 抓取失败: {url} | 错误: {e}")
        # 如果遇到报错，多休息一会儿，防止被彻底拉黑
        time.sleep(5)

print("\n" + "="*40)
print(f"🎉 批量下载完成！成功: {success_count} 个，失败: {fail_count} 个。")
print("over!")