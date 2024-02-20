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
T_cur=dic[Cur]
dr=webdriver.Chrome()
dr.get("https://srh.bankofchina.com/search/whpj/search_cn.jsp")
from selenium.webdriver.support.select import Select
select=dr.find_element(By.ID,"pjname")
options_list = Select(select).options
for option in options_list:
    print(option.text)
Select(select).select_by_value(T_cur)
#完成国家货币选择
date_field = dr.find_element(By.NAME,"erectDate")
date_field.clear()
date_field.send_keys(date)
date_field.submit()
date_field = dr.find_element(By.NAME,"nothing")
date_field.clear()
date_field.send_keys(date)
date_field.submit()
cur_name=dr.find_elements(By.CSS_SELECTOR,'table tbody tr:nth-child(2) td:nth-child(4)')
for x in cur_name:
    print(x.text)
    break
#输入是时间和货币代码
#输出是卖出价
