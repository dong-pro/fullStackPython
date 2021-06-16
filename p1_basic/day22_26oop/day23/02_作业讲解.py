# # 15题 字典也是类
# class User:
#     def __init__(self, user, pwd, email):
#         self.user = user
#         self.pwd = pwd
#         self.email = email
#
# user_list = []
#
# # obj = User('alex1', '123', 'xx@live.com')
# obj = {'user': 'alex1', 'pwd': 123,
#        'email': 'asdf@live.com'}  # dict({'user':'alex1','pwd':123,'email':'asdf@live.com'})
# user_list.append(obj)
#
# # obj = User('alex2', '123', 'xx@live.com')
# obj = {'user': 'alex1', 'pwd': 123, 'email': 'asdf@live.com'}
# user_list.append(obj)
#
# # obj = User('alex3', '123', 'xx@live.com')
# obj = {'user': 'alex1', 'pwd': 123, 'email': 'asdf@live.com'}
# user_list.append(obj)
#
# for row in user_list:
#     # print(row.user, row.pwd, row.email)
#     print(row['user'], row['pwd'], row['emailr'])


# 16题
class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

class Account:
    def __init__(self):
        self.user_list = []

    def login(self):
        name = input('请输入账号:')
        pwd = input('请输入密码:')
        flag = False
        for user in self.user_list:
            if name == user.name and pwd == user.pwd:
                flag = True
                break
        if flag:
            print('登录成功')
        else:
            print('登录失败')

    def register(self):
        i = 0
        while i < 3:
            i += 1
            name = input('请输入用户名:')
            pwd = input('请设置密码:')
            usr = User(name, pwd)
            self.user_list.append(usr)

    def run(self):
        self.register()
        self.login()

if __name__ == '__main__':
    obj = Account()
    obj.run()
