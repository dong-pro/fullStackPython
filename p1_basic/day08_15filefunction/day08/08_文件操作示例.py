lst = []
with open('问题合集',mode='r',encoding='utf-8') as f:
    first = f.readline().strip().split(',')
    print(first)
    for line in f:
        dic = {}
        con = line.strip().split(',')
        for i in range(len(first)):
            if i < len(con):  # 避免索引越界
                dic[first[i]] = con[i]
            else:
                dic[first[i]] = ''  # 缺失值填充为空字符串
        lst.append(dic)
print(lst)


# 方法2:用标准库 csv 替代手动分割（更专业处理 CSV 文件，支持逗号转义、换行等特殊情况）：
import csv
lst = []
with open('问题合集', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)  # 自动将第一行作为字段名
    for row in reader:
        lst.append(dict(row))  # 每行直接是字典，转换后追加
print(lst)
