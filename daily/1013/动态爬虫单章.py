import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

URL = "https://www.bqg420.cc/#/book/1499/1.html"

print("正在启动 Chrome 浏览器...")
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--remote-allow-origins=*')

    # 1. 【新增】在 try 之前，声明 driver 为空
driver = None 
try:
    # 假设你的代码在 1013 文件夹下
    service = Service(executable_path=r'D:\新建文件夹\python\01class\1013\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # ... 后面的代码 (提取正文等) ...
    
    driver.get(URL)
    time.sleep(5) # 等待 JavaScript 渲染
    
    html_content = driver.page_source
    
    # ============ 新的提取逻辑 ============
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 1. 直接找 body 标签（既然找不到特定的 div，我们就找整个 body）
    body = soup.find('body')
    
    if body:
        # 2. 关键操作：先把网页里所有的 <br> 标签替换成纯文本换行符 \n
        # 因为 <br> 在 HTML 里就是换行的意思，BeautifulSoup 默认会把它当纯文本粘在一起
        html_str = str(body)
        html_str = html_str.replace('<br>', '\n').replace('<br/>', '\n').replace('<br />', '\n')
        
        # 3. 重新用 BeautifulSoup 解析替换后的纯文本，去掉其他 HTML 标签
        clean_soup = BeautifulSoup(html_str, 'html.parser')
        text = clean_soup.get_text(strip=True)
        
        # 4. 保存
        with open("小说单章测试.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("[OK] 成功提取正文！已保存为 '小说单章测试.txt'")
    else:
        print("[警告] 没有找到 body 标签！")

except Exception as e:
    # 这里会打印出真正的错误原因
    print(f"[ERROR] 发生错误：\n{e}")

finally:
    # 2. 【修改】只有 driver 存在时才去 quit
    if driver:
        driver.quit()
    print("测试结束。")










