from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import time
import requests
import csv
import random
url = 'https://www.backpackers.com.tw/forum/forumdisplay.php?f=60'

chromepath = r'C:\Users\d8546\Google 雲端硬碟\PyETL 爬蟲\PycharmProjects\SPOTS\venv\chromedriver.exe'
browser = webdriver.Chrome(chromepath)
browser.get(pageurl)

#被封鎖IP了嗎
if __name__ == '__main__':
    # 代理伺服器查詢: http://cn-proxy.com/
    proxy_ips = ['51.15.227.220:3128', '81.162.56.154:8081']
    ip = random.choice(proxy_ips)
    print('Use', ip)
    resp = requests.get('http://ip.filefab.com/index.php',
                        proxies={'http': 'http://' + ip})
    soup = BeautifulSoup(resp.text, 'html5lib')
print(soup.find('h1', id='ipd').text.strip())

head = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Mobile Safari/537.36'}

# getting data
response = requests.get("https://www.backpackers.com.tw/forum/forumdisplay.php?f=60")
#確認網站狀態
print(response.status_code)
soup = BeautifulSoup(response.text, 'lxml')
print(soup.find("strong"))
# parsing data
#d = pq(url.str)
#rating_selector = "strong span"
#rating = [float(i.text()) for i in d(rating_selector).items()][0]
#print(type(d))
#print(d(rating_selector))
#print(rating)

#找出所有內容
#Signature: re.findall(pattern, string, flags)
pattern = "我寫好的regular expression"
re.findall(pattern, string)

#使用for迴圈翻頁，
for i in range(1,100):
    url='https://www.backpackers.com.tw/forum/'+str(i)