import os

# # 1、写一个函数，接受一个参数，如果是文件，就执行这个文件，如果是文件夹，就执行这个文件夹下所有的py文件
# def func(path):
#     # 先判断这个path是文件还是文件夹,isdir isfile
#     # 如果是文件,.py结尾的
#     if os.path.isfile(path) and path.endswith('.py'):
#         # 执行这个文件 :
#         os.system('python %s' % path)  # 模拟了在cmd中执行代码的过程
#     # 如果是文件夹
#     elif os.path.isdir(path):
#         # 查看这个文件夹下的所有内容  listdir
#         for name in os.listdir(path):
#             abs_path = os.path.join(path, name)
#             # 如果是文件 .py结尾的
#             if abs_path.endswith('.py'):
#                 # 执行这个文件 : os.system('python %s'%abs_path)
#                 os.system('python %s' % abs_path)
#
# func(r'D:\sylar\s15\day19\7.json模块.py')
# func(r'D:\sylar\s15\day19')


# # 2、写一个copy函数，接收两个参数，第一个参数是源文件的位置，第二个参数是目标位置，将源文件copy到目标位置。
# # 还需要判断一下这个文件之前是否存在
# def copy(path1, path2):
#     filename = os.path.basename(path1)
#     if os.path.isfile(path1) and os.path.isdir(path2):
#         path2 = os.path.join(path2, filename)
#         if os.path.exists(path2):
#             print('已有同名文件')
#         with open(path1, 'rb') as f1, open(os.path.join(path2, filename), 'wb') as f2:
#             content = f1.read()
#             f2.write(content)
#
# copy(r'D:\sylar\s15\day19\01_今日内容大纲.py', r'D:\sylar\s15\day18')

# # 3、获取某个文件所在目录的上一级目录。
# # 例如'D:\sylar\s15\day19\6.序列化模块.py'目录的结果 ：D:\sylar\s15
# # 方法1
# path = os.path.dirname(r'D:\sylar\s15\day19\6.序列化模块.py')
# base_name = os.path.dirname(path)
# print(base_name)
# # 方法2
# base_name = os.path.dirname(os.path.dirname(r'D:\sylar\s15\day19\6.序列化模块.py'))
# print(base_name)

# 4、使用os模块创建如下目录结构
# glance/
#
# ├── __init__.py
#
# ├── api
#
# │   ├── __init__.py
#
# │   ├── policy.py
#
# │   └── versions.py
#
# ├── cmd
#
# │   ├── __init__.py
#
# │   └── manage.py
#
# └── db
#
#     ├── __init__.py
#
#     └── models.py
# # 创建文件夹
# # 创建文件
# os.makedirs('glance/api')
# os.makedirs('glance/cmd')
# os.makedirs('glance/db')
# open('glance/api/__init__.py', 'w').close()
# open('glance/api/policy.py', 'w').close()
# open('glance/api/versions.py', 'w').close()
# open('glance/cmd/__init__.py', 'w').close()
# open('glance/cmd/manage.py', 'w').close()
# open('glance/db/__init__.py', 'w').close()
# open('glance/db/models.py', 'w').close()

# # 5、写一个用户注册登陆的程序，每一个用户的注册都要把用户名和密码用字典的格式写入文件userinfo。
# # 在登陆的时候，再从文件中读取信息进行验证。
# {'usr': 'alex', 'pwd': 'alex3714'}
# import pickle
#
# def register():
#     usr = input('username:')
#     pwd = input('password:')
#     dic = {usr: pwd}
#     with open('userinfo', 'ab') as f:
#         pickle.dump(dic, f)
#     print('注册成功')
#
# def login():
#     flag = True
#     usr = input('username :')
#     pwd = input('password : ')
#     with open('userinfo', 'rb') as f:
#         while flag:
#             try:
#                 dic = pickle.load(f)
#                 for k, v in dic.items():
#                     if k == usr and pwd == v:
#                         print('登录成功')
#                         flag = False
#                         break
#             except EOFError:
#                 print('登录失败')
#                 break
#
# register()
# login()

# 6、发红包  random
import random
# 更好
# def red_packet(money, num):
#     money = money * 100  # 将钱转换成分
#     ret = random.sample(range(1, money), num - 1)
#     ret.sort()
#     ret.insert(0, 0)
#     ret.append(money)
#     for i in range(len(ret) - 1):
#         yield (ret[i + 1] - ret[i]) / 100
#
# ret_g = red_packet(200, 10)
# for money in ret_g:
#     print(money)


# def Bonus(person, money):  # 5,200
#     dict_person_money = {}
#     for i in range(person):
#         num = random.randint(1, 100)  # 99 99 99 99 99
#         dict_person_money["Person%s" % (i + 1)] = num  # person1:99
#     num_sum = 0
#     for i in dict_person_money:
#         num_sum += dict_person_money[i]  # 5 * 99 = 495
#     for i in dict_person_money:  # 99/495 1/5 * 200 = 40
#         x = round(dict_person_money[i] / num_sum * money, 2)
#         dict_person_money[i] = '$%s' % x
#     return dict_person_money
#
# result = Bonus(10, 1)
# print(result)


# def hongbao(sum, n):
#     lst = []
#     for i in range(n - 1):
#         number = random.uniform(0, sum)
#         number = round(number, 2)  # 保留两位小数
#         sum = sum - number
#         lst.append(number)
#     lst.append(sum)
#     random.shuffle(lst)
#     return lst
#
# lst = hongbao(100, 5)
# print(lst)


# def red_envelopes(money, numbers=10):
#     name_list = ['梁慧', '蒲雪', '刘宁谦', '侯明魏', '尚红运',
#                  '刘晓蕾', '杨文状', '姚尚', '冯俊才', '宋华生']
#     sum_n = 0
#     balance = money
#
#     for index, name in enumerate(name_list):
#         random_money = random.uniform(0, balance / 3)
#         if index == numbers - 1:
#             print('%s grabbed %.2f element'
#                   % (name, money - sum_n))
#         else:
#             balance -= random_money
#             sum_n += random_money
#             print('%s grabbed %.2f element'
#                   % (name, random_money))
#
#
# money = int(input('please enter the amount of your red envelope!'))
# red_envelopes(money)


# # 7、计算器
# # '3+4' '5*6' '2-5' '5/2'
# # 写函数 计算小字符串的结果
#
# # 1*2+3-4/5
# # 乘或者除法先匹配出来
#
# # 小数的 '3.2+4.5' '5.0*6' '2-5' '5/2'
#
# # 默写:
# # 计算文件夹的大小 : 递归/循环
