# 以前写法
# data_list = []
#
# for i in range(1, 901):
#     data_list.append('alex-%s' % i)
#
# while True:
#     # 1. 要查看的页面
#     page = int(input('请输入要查看的页码:'))
#
#     # 2. 每页显示 10 条
#     per_page_num = 10
#
#     start = (page-1) * per_page_num
#     end = page * per_page_num
#
#     page_data_list = data_list[start:end]
#     for item in page_data_list:
#         print(item)


class Pagenation(object):
    """
    处理分页相关的代码
    """
    def __init__(self, data_list, page, per_page_num=10):
        """
        初始化
        :param data_list: 所有的数据
        :param page: 当前要查看的页面
        :param per_page_num: 每页默认要显示的数据行数
        """
        self.data_list = data_list
        self.page = page
        self.per_page_num = per_page_num

    @property
    def start(self):
        """
        计算索引的起始位置
        :return:
        """
        return (self.page - 1) * self.per_page_num

    @property
    def end(self):
        """
        计算索引的结束位置
        :return:
        """
        return self.page * self.per_page_num

    def show(self):
        result = self.data_list[self.start:self.end]
        for row in result:
            print(row)

data_list = []
for i in range(1, 901):
    data_list.append('alex-%s' % i)

while True:
    # 1. 要查看的页面
    page = int(input('请输入要查看的页码:'))
    obj = Pagenation(data_list, page)
    obj.show()
