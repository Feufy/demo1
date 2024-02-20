from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 创建 WebDriver 实例对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome()

# WebDriver 实例对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.11meigui.com/tools/currency')
dic=dict()
time.sleep(5)

cur_name=wd.find_elements(By.CSS_SELECTOR,'table tbody tr:nth-child(2) td:nth-child(2)')
cur_id=wd.find_elements(By.CSS_SELECTOR,'table tbody tr:nth-child(2) td:nth-child(5)')
l_name=list()
for name in cur_name:
    if name.text=='中文' or name.text=='货币符号' or name.text=='货币名称' or name.text=='英文':
        continue
    else:
        l_name.append(name.text)
for id,name in zip(cur_id,l_name):
        dic[id.text]=name
        print(id.text+":"+name)
#第一步：完成英文缩写和全称的对应，将其保留在dic字典中
#第二步：依据输入时间和输入代号获取最终
wd.quit()
date=input()
Cur=input()
dr=webdriver.Chrome()
dr.get("https://srh.bankofchina.com/search/whpj/search_cn.jsp")

