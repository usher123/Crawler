import pickle
import re
def select_link(links):
    check_link = {}
    dict_links = open('text.txt','r')
    try:
        check_link = pickle.load(dict_links)
    except EOFError:
        check_link['http://news.baidu.com'] = 'news.baidu.com'
    dict_links = open('text.txt','w')
    save_link = open ('href_links.txt','a')
    for link in links:
        wp = re.match('.*\.baidu\.com.*',link)
        if wp == 'None':
            if link not in check_link:
                if link+'/' not in check_link:
                    try:
                        if link[len(link)-1] == '/' and link[:len(link)-1] not in check_link: 
                            check_link[link] = link
                            save_link.write(link+'\n')
                    except IndexError:
                        print ('string index out of range')
    pickle.dump(check_link,dict_links,0)
    dict_links.close()
    save_link.close()

        
            


