import urllib
import re
import time
from bs4 import BeautifulSoup

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def getBookname(url):
    soup=BeautifulSoup(html)
    bookname=soup.find_all('img')
    x=1
    for name in bookname:
        urllib.urlretrieve(name['src'],"%s.jpg"%name['alt'])
        print name['src']
        time.sleep(1)
        x+=1
html=getHtml("http://book.douban.com")

getBookname(html)
