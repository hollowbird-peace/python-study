import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# 起始章节的网址
START_URL = "https://www.bqg420.cc/#/book/1499/1.html" 

# 要下载多少章
TOTAL_CHAPTERS = 5

print("正在启动 Chrome 浏览器...")
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--remote-allow-origins=*')

driver = None

try:
    service = Service(executable_path=r'D:\新建文件夹\python\01class\1013\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # 1. 打开第一章
    driver.get(START_URL)
    time.sleep(5) # 等待渲染
    
    # 用来存放整本小说
    full_novel = ""

    # 2. 开始循环抓取
    for chapter in range(TOTAL_CHAPTERS):
        print(f"正在抓取第 {chapter + 1} 章...")
        
        # 获取网页源码并解析
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # 使用我们上次确认过的 <br> 替换逻辑
        body = soup.find('body')
        if body:
            html_str = str(body).replace('<br>', '\n').replace('<br/>', '\n').replace('<br />', '\n')
            clean_soup = BeautifulSoup(html_str, 'html.parser')
            text = clean_soup.get_text(strip=True)
            
            # 提取章节标题（通常在第一行，或者 h1 标签里，这里简单截取前 20 个字作为标记）
            title = text[:20].replace('\n', ' ') 
            
            full_novel += f"\n\n===== {title} =====\n\n{text}"
            print(f"[OK] 第 {chapter + 1} 章抓取成功！")
        
        # 3. 寻找并点击“下一章”
        try:
            # 这一步很关键：你需要去网页源码里找“下一章”按钮对应的 HTML 标签
            # 假设它的链接文字叫“下一章”，或者它的 class 叫 "next"
            # 我给出几种常见的寻找方式：
            next_button = driver.find_element(By.PARTIAL_LINK_TEXT, "下一章") # 按文字找
            
            # 如果没有找到，尝试按 class 找（比如 class="next"）
            # next_button = driver.find_element(By.CLASS_NAME, "next") 
            
            next_button.click() # 点击下一章
            time.sleep(4) # 点击后，等待新章节加载出来
        except Exception as e:
            print(f"❌ 没找到下一章按钮，可能已经是大结局了，或者标签名不对。错误：{e}")
            break # 找不到下一章就跳出循环

    # 4. 保存整本小说
    with open("小说多章测试.txt", "w", encoding="utf-8") as f:
        f.write(full_novel)
    print("[OK] 全书抓取完成！已保存为 '小说多章测试.txt'")

except Exception as e:
    print(f"[ERROR] 发生错误：\n{e}")

finally:
    if driver:
        driver.quit()
    print("浏览器已关闭，测试结束。")