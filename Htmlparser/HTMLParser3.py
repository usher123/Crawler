import urllib
import re
import os
import sys
import socket
from select_link import select_link
from HTMLParser import HTMLParser
from charset import charset
class MyHTMLParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.flag = 0
            self.links = []
            self.title=""
            self.other = []
        def handle_starttag(self, tag, attrs):
            if tag == "a"  :
                if len(attrs) == 0: pass
                else:
                    for (variable, value)  in attrs:
                        if variable == "href":
                            try:
                                self.links.append(value.encode('utf8','ignore'))
                            except AttributeError:
                                ptint('encode erro')

            if tag =="href":
                self.flag=1
            if tag == "img":
                for (name,value) in attrs:
                    if name =='src':
                        self.other.append(value)

        def handle_data(self,data):
            if self.flag == 1 and len(self.href)==0:
                self.href=data
                self.flag==0

def save_htmlpage(url,size):
    print(url)
    ds = open ('grap.txt','a')
    try:
        page = urllib.urlopen(url).read()
    except IOError: ## erro need to change
        print('this href link too long')
        ds.close()
        return  'abon-link'
        
    try:
        page.decode(size)
    except UnicodeDecodeError:
        __int__("utf-8")
        size ="utf-8"
        try:
            page.decode(size,'ignore')
        except UnicodeDecodeError:
            print('decode error')
    ds.write(page.decode(size,'ignore'))
    ds.write('\n'+"<=========================================================================================(___Tag___)=========================================================================================================>"+'\n')
    ds.close()
    return page.decode(size,'ignore')

def __int__(size):
    reload(sys)
    sys.setdefaultencoding(size)

def save_link(url,size):
    data = save_htmlpage(url,size)
    if data == 'abon-erro':
        return False
    wp = MyHTMLParser()
    wp.feed(data)
    gs = open('image_links.txt','wb')
    select_link(wp.links) 
    for imag in wp.other:
        gs.write(imag +'\n')
    gs.close()


def true_link(link):
    if 1:           'need changing to urllib get 200 '
        return True
    else:
        return False


if __name__ == "__main__":
    socket.setdefaulttimeout(3)
    file = open('href_links.txt','r')
    url = "http://news.baidu.com"
    size = charset(url)
    __int__(size)
    save_link(url,size)
    l = 'y'
    while l != 'no':
        n=1
        while n != 0:
            link = file.readline()
            if link == "tag\n":
                l =raw_input('this is tagbull,do you want to go on:\'y\' or\'n\'' )
                if l == 'yes':
                    n = 1
                    incm = open('href_links.txt','a')
                    incm.write('tag'+'\n')
                    incm.close()
                    link = file.readline()
                if l == 'no':
                    print('bye-bye')
                    exit()
            if true_link(link) == True:
                n = 0
        size = charset(link)
## while size == 'time out':
##            link = file.readline()
##            size = charset(link)
        __int__(size)
        save_link(link,size)
    bs.close()
    file.close()   

