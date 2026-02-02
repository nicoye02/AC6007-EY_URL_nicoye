import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_business_description(url):
    try:
        # 1. 抓取
        headers = {'User-Agent': 'Mozilla/5.0...'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # 核心修复点：直接解析 response.text 字符串
        html_content = response.text 
        
        # 确保不要在这里调用 open(html_content)
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 2. 提取文本
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        text_content = " ".join(paragraphs[:5])
        
        return text_content, ""
        
    except Exception as e:
        return f"抓取失败: {str(e)}", ""