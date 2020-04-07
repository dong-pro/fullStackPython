from lzl import Nb


def baidu_repsonse(body):
    print('百度下载结果：', body)


def sogou_repsonse(body):
    print('搜狗下载结果：', body)


def oldboyedu_repsonse(body):
    print('老男孩下载结果：', body)


t1 = Nb()
t1.add('www.baidu.com', baidu_repsonse)
t1.add('www.sogou.com', sogou_repsonse)
t1.add('www.oldboyedu.com', oldboyedu_repsonse)
t1.run()
