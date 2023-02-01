from urllib.request import urlopen, Request
import ssl

# 解决网站的反爬虫机制
url = 'https://movie.douban.com/top250?start=50&filter='
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
context = ssl._create_unverified_context()

ret = Request(url,headers=headers)
res = urlopen(ret,context=context).read().decode('utf-8')
print(res)