domain = 'http://www.backpackers.com.tw/forum/showthread.php?s=6ec6162b5de5254263fc62bac5ae53bf&t='
ba = []

from bs4 import BeautifulSoup as bs
import re

for j in range(1, 1344):

    f = open('project5/bag11/{}.txt'.format(j), 'r')

    a = f.read()
    soup = bs(a)
    td = soup('td')[0]['id']  # 景點id
    a11 = td.split('_')[2]  #
    a12 = simple2tradition(a11.encode('utf-8'))
    print
    a12

    soup = bs(a)  # 發文日期
    a = soup.select('.smallfont')[0]
    b = a.text.split(',')
    c = b[0]
    m = re.search('.*(20(\d.*))', c)
    b11 = m.group(1)
    b12 = simple2tradition(b11.encode('utf-8'))
    print
    b12

    strong = soup.select('strong')  # 遊記標題
    c11 = strong[0].text.split('-')[0]
    c12 = simple2tradition(c11.encode('utf-8'))
    print
    c12

    vb_postbit = soup.select('.vb_postbit')  # 遊記內容
    d11 = vb_postbit[0].text
    d12 = simple2tradition(d11.encode('utf-8'))
    print
    d12

    res = str(soup)  # 來源網址 先把soup轉成字串型式
    try:
        m2 = re.search(
            '<a href=\"http:\/\/www.facebook.com\/sharer.php\?u=http%3A%2F%2Fwww.backpackers.com.tw%2Fforum\%2Fshowthread.php%3Ft\%3D(.*?)\"',
            res)
    except AttributeError:
        print
        j, 'urlempty'
    print
    domain + m2.group(1)

    print
    '背包客棧'
    f = open('project5/bagfinal123/{}.txt'.format(j), 'w')
    f.write(a12 + '||||||||||' + b12 + '||||||||||' + c12 + '||||||||||' + d12 + '||||||||||' + domain + m2.group(
        1) + '||||||||||' + '背包客棧')
    f.close()
