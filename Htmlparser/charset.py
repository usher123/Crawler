import urllib
def charset(url):
    w = 0
    try:
        data = urllib.urlopen(url)
        word1 = data.readline()
    except IOError:
        return 'time out'
    if 'charset=' in word1:
        word0 =word1
        w = 1
    n=0
    i=0
    c=0
    o=0
    while 'charset=' not in word1 and i !=1 and word1 != '':
        word1 = data.readline()
        if 'charset="' in word1:
            word2 = word1
            n=1
            i=1
            c=1
        if 'charset=\'' in word1:
            word3 = word1
            n=2
            i=1
            c=1
        if 'charset=' in word1 and c != 1:
            word4 = word1
            n=3
            i=1
    if n == 0 and w != 1:
        print "No-chase"
        return "utf-8"
        
    if n == 0 and w == 1:
        if 'charset="' in word0:
            n=1
            o=1
            word2 = word0
        if 'charset=\'' in word0 and o !=1:
            n=2
            o=1
            word3 = word0
        if 'charset=' in word0 and o !=1:
            n=3
            o=1
            word4 = word0
    if n == 1:
        use = word2.split('charset="')[1]
        new = use.split('"')[0]
        return new
    if n == 2: 
        use = word3 .split('charset=\'')[1]
        new = use.split('\'')[0]
        return new
    if n == 3:
        use = word4 .split('charset=')[1]
        new = use.split('"')[0]
        return new
'''if __name__ =="__main__":
    a = 'http://www.baidu.com/more/'
    w = charset(a)
    print w'''
