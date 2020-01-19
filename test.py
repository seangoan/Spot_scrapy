import requests
from bs4 import BeautifulSoup
head = 'https://www.backpackers.com.tw/forum/forumdisplay.php?f=60'
res = requests.get(head)

print(res.text)

