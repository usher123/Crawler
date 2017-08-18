import os
print'push down ctrl + d\n'
os.system('cat > aha.json')
print('begin!\n')
os.system('scrapy crawl johns -o aha.json -t json')

