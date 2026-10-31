import os
from bs4 import BeautifulSoup

# ================= 配置区域 =================
# 你下载的所有 html 文件所在的文件夹名
HTML_FOLDER = 'biqubee_novel_all'  
# 最终生成的小说文件名
OUTPUT_FILE = '蛊真人_全本.txt'
# ===========================================

# 1. 找到所有 html 文件，并按文件名排序（保证章节顺序正确）
all_files = sorted([f for f in os.listdir(HTML_FOLDER) if f.endswith('.html')])
print(f"共找到 {len(all_files)} 个章节文件，准备开始提取...")

# 新增这行，看看前5个文件名是什么
print("前5个文件:", all_files[:5]) 

# 用来存放提取出来的整本小说文本
novel_text = ""

# 2. 遍历每个文件进行提取
for filename in all_files:
    filepath = os.path.join(HTML_FOLDER, filename)
    
    try:
        # 读取 HTML 内容
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 查找正文
        content_div = soup.find('div', class_='showtxt')
        if not content_div:
            content_div = soup.find('div', id='Content')
        
        if content_div:
            # 提取纯文本
            text = content_div.get_text(separator='\n', strip=True)
            
            # ================= 核心修复点：在这里定义并替换 =================
            # 1. 定义要替换的拼音字典
            fix_dict = {
                'sè': '色',
                'sāo': '骚',
                'yīn': '阴',
                'chūn': '春',
                'xìng': '性',
                'zhōngyāng': '中央',
                'hǎohàn': '浩瀚',
                # 以后继续往这里加
            }
            
            # 2. 遍历字典，执行替换
            for pinyin, chinese in fix_dict.items():
                text = text.replace(pinyin, chinese)
            # ==============================================================
            
            novel_text += text + "\n\n"
            print(f"✅ 成功提取: {filename}")
            
        else:
            print(f"⚠️ 未找到正文标签，跳过: {filename}")
            
    except Exception as e:
        print(f"❌ 读取失败: {filename}, 错误: {e}")
    
try:
    # 读取 HTML 内容
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    # 尝试1：根据你截图里那个独特的 class 名来查找
    content_div = soup.find('div', class_='showtxt')

# 如果还是找不到，再尝试用 id 找（因为有时候 class 会变）
    if not content_div:
        content_div = soup.find('div', id='Content') 

# 新增这行，看看有没有抓到
    if content_div:
        print(f"✅ 在 {filename} 里抓到了正文标签")
    else:
        print(f"❌ 在 {filename} 里没找到 <div id='Content'>")
    
    # 【关键！】这里必须有一个 if 来跟下面的 else 配对
    if content_div:  
        text = content_div.get_text(separator='\n', strip=True)
        
        # 拼音替换逻辑...
        for pinyin, chinese in fix_dict.items():
            text = text.replace(pinyin, chinese)
        
        novel_text += text + "\n\n"
        print(f"✅ 成功提取: {filename}")
        
    else:  # <--- 这个 else 必须跟上面的 if 对齐
        print(f"⚠️ 未找到正文标签，跳过: {filename}")
        
except Exception as e: # <--- except 必须跟 try 对齐
    print(f"❌ 读取失败: {filename}, 错误: {e}")
# 5. 保存最终的 TXT 文件
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(novel_text)

print(f"\n🎉 合并完成！你的小说已保存为：{OUTPUT_FILE}")