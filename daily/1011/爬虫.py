import urllib.request
from urllib.request import Request, urlopen

url = "https://www.biqubee.com/bi_7280/0.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}

req = Request(url, headers=headers)
resp = urlopen(req)
html_content = resp.read().decode('utf-8', errors='ignore')
import time
import os
save_folder = r'D:\新建文件夹\python\01class\1011'
save_path = os.path.join(save_folder, f'biqubee_{int(time.time())}.html')

print(f"即将保存到: {save_path}") 
with open(save_path, mode='w', encoding='utf-8') as f:
    f.write(html_content)
print('over!')