import urllib.request
from urllib.request import Request, urlopen
import time
import os
import random
import ssl

# 1. 把你要爬的所有网址放进一个列表里
url_list = []
for i in range(1,6):
    url_list.append(f"https://www.biqubee.com/bi_7280/{i}.html")
    url_list.append(f"https://www.biqubee.com/bi_7280/{i}_2.html")

# 2. 设置请求头（伪装成浏览器）
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}

# 3. 创建一个文件夹来专门存放下载下来的网页（避免文件乱放）
# 如果文件夹不存在，就自动创建
save_folder = 'biqubee_novel'
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# 4. 开始循环爬取
print("开始爬取，请稍候...")
for index, url in enumerate(url_list):
    try:
        # 构造请求并发送
        req = Request(url, headers=headers)
        # 创建一个忽略 SSL 证书验证的上下文
        context = ssl._create_unverified_context()

# 把 context 传给 urlopen
        resp = urlopen(req, context=context)
        
        # 读取内容并解码
        html_content = resp.read().decode('utf-8', errors='ignore')
        
        # 5. 提取文件名（例如从 url 中提取 "1.html" 作为文件名）
        # 如果直接以网址结尾做文件名，比如 1.html，多线程下容易冲突，但这里单线程没问题
        # 这里我们用递增的序号命名，比如 01_1.html, 02_1_2.html，方便排序
        filename = f"{index+1:02d}_{url.split('/')[-1]}"
        filepath = os.path.join(save_folder, filename)
        
        # 6. 保存文件
        with open(filepath, mode='w', encoding='utf-8') as f:
            f.write(html_content)
            
        print(f"✅ 成功抓取: {url} -> 已保存为 {filepath}")
        
        # 7. 【关键！】每次爬完一个页面，强制休息 1-2 秒
        # 这是为了防止请求太快，被对方服务器发现并封禁你的 IP
        time.sleep(random.uniform(1.5, 2.5)) # 注意：需要在顶部导入 import random
        
    except Exception as e:
        print(f"❌ 抓取失败: {url}, 错误信息: {e}")

print("全部抓取完成！over!")