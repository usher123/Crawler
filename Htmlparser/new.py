import pickle
import os
def new():
    os.system('cat > href_links.txt')
    os.system('cat > grap.txt')
    a={}
    b=open('text.txt','w')
    pickle.dump(a,b,0)
    b.close()
if __name__ =='__main__':
    new()


