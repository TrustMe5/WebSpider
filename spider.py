#coding:utf-8
import re
import os
import urllib
import urllib2
from bs4 import BeautifulSoup
import time
class Spider:
      def __init__(self):
          self.url="http://book.douban.com"

      def getPage(self,url):
          request=urllib2.Request(url) 
          response=urllib2.urlopen(request)
          page=response.read()
          return page

      def getContent(self):
          page=self.getPage(self.url)
          pattern=re.compile('<div class="cover".*?<a.*?title="(.*?)".*?href="(.*?)".*?<img.*?alt="(.*?)".*?src="(.*?)"',re.S)
          listlist=re.findall(pattern,page)
          x=1
          for li in listlist:
              print "%s :"%x,u"书名：",li[0],u"书的链接：",li[1],u"书名：",li[2],u"书皮图片链接：",li[3]
              self.makedir(li[0])
              self.savebookimgurl(li[3],li[0])
              self.savebooklianjie(li[1],li[0],'图书链接地址')
              self.getDetailbookinfo(li[1],li[0])
              self.saveImg(li[3],li[0])
              x+=1
              time.sleep(1)

      def saveImg(self,imgurl,filename):
          filename=filename+'/'+filename
          htm=urllib2.urlopen(imgurl)
          data=htm.read()
          f=open(filename,'wb')
          f.write(data)
          f.close()
  
      def makedir(self,filename):
          isexists=os.path.exists(filename)
          if not isexists:
             os.makedirs(filename)
             return True
          else:
             return False

      def savebookimgurl(self,content,name):
          file=name+'/'+name+'的图片链接'
          f=open(file,'a')
          f.write(content)
          f.close()

      def savebookintro(self,content,name,filename):
          info=name+'/'+filename+'.txt'
          f=open(info,'a')
          f.write(content)
          f.close()

      def savebooklianjie(self,content,name,filename):
          file=name+'/'+filename
          f=open(file,'a')
          f.write(content)
          f.close()

      def getDetailbookinfo(self,url,name):
          page=self.getPage(url)
          pattern=re.compile('<div class="intro".*?<p>(.*?)</p>',re.S)
          bookinfo=re.findall(pattern,page)
          for book in bookinfo:
              self.savebookintro(book,name,'图书简介')
    
    
spider=Spider()
spider.getContent()
