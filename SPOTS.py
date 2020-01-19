import requests # 連結網址
from bs4 import BeautifulSoup # 轉HTML成為PYTHON可用物件，並且可以定位。
import urllib.request # 下載圖片
import os # 新增資料匣

dir = "Spots"
if not os.path.exists(dir):
    os.mkdir(dir)

url = 'https://www.backpackers.com.tw/forum/forumdisplay.php?f=177'
# Request headers 用字串灌進來
headers_str = """authority: www.backpackers.com.tw
method: GET
path: /; domain=.backpackers.com.tw
scheme: https
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36
headers = {}
# 一次處理全部的headers，用字典處理的概念。
for row in headers_str.split('\n'):
    headers[row.split(': ')[0]] = row.split(': ')[1]


# 處理Cookies用，request_session可以讀到一整包東西，就是網頁若自己幫你加cookies，它會自行處理，但基本的還是要幫他弄。
request_session = requests.session()

n = int(input('讀取幾頁?'))
for page_num in range(0, n):
# 讀取網頁，讀成電腦的語言。
    response = request_session.get(url, headers = headers)
    response.encoding = 'utf-8'

    # soup是轉成HTML語法
    soup_first = BeautifulSoup(response.text, 'html.parser') # text, 'html.parser 綁定的'


    page_all_titles = soup_first.select('div[class="title"]')

    for page_title_num, each_title in enumerate(page_all_titles):
        try: # 處理標題已刪文。
            url= 'www.backpackers.com.tw' + each_title.a['href']
        except:
            pass
        response = request_session.get(url, headers = headers)
        response.encoding = 'utf-8'
        soup_second = BeautifulSoup(response.text, 'html.parser')
        img_num = 0
        for a_tag in (soup_second.select('a')):
            if ('.jpg' in a_tag['href']):
                img_num += 1
                img_url = a_tag['href']
                response = urllib.request.urlopen(img_url)
                img_content = response.read()
                with open('./%s/%d頁%d篇.%d張.jpg' % (dir, page_num + 1, page_title_num + 1, img_num), 'wb') as f:
                    f.write(img_content)

    url = 'www.backpackers.com.tw' + soup_first.select('div[class="btn-group btn-group-paging"]')[0].select('a')[1]['href'] #跳到下一頁
