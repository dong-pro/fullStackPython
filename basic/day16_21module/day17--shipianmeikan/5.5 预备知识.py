from urllib import request
ret = request.urlopen('https://movie.douban.com/top250?start=50&filter=')
res = ret.read().decode('utf-8')
print(res)