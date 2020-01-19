from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import time
import requests
import csv

pageurl = 'https://www.backpackers.com.tw/forum/forumdisplay.php?f=60'
chromepath = r'C:\Users\d8546\Google 雲端硬碟\PyETL 爬蟲\PycharmProjects\SPOTS\venv\chromedriver.exe'
browser = webdriver.Chrome(chromepath)
browser.get(pageurl)
soup = BeautifulSoup(browser.page_source, 'lxml')

url = 'http://www.backpackers.com.tw/forum/'
head = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Mobile Safari/537.36'}

fin = []
pg = 1

while True:
    i = 0
    print(pg)
    for wb in soup.select('#threadbits_forum_60 tr'):  # 每頁資訊
        if i > 0:
            print('===============' + str(i) + '===============')
            print(wb.select('div a')[0]['href'])
            urlf = url + wb.select('div a')[-2]['href']  # 每篇發文網頁合併
            # print(urlf)
            req = requests.get(urlf, headers=head)  # 取得發文內容
            soupf = BeautifulSoup(req.text, 'lxml')

            print(soupf.select('h1 strong')[0].text)  # 標題
            # print(soupf.select('.vb_postbit')[0].text) #內文
            fin.append([soupf.select('h1 strong')[0].text, soupf.select('.vb_postbit')[0].text, urlf])
            time.sleep(0.5)
        i += 1
    if len(soup.find_all(attrs={'rel': 'next'})) == 0 or pg == 30:  # 當沒有next按鈕時 中斷迴圈
        break
    elif pg % 10 == 0:
        j = 1
        with open('台灣北部' + str(j) + '.csv', 'w', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerows(fin)
        del fin[:]

    browser.find_element_by_xpath(u"(//a[contains(text(),'下頁')])[2]").click()
    soup = BeautifulSoup(browser.page_source, 'lxml')
    pg += 1

browser.close()
