class Account:
    def login(self):
        user = input('请输入用户名:')
        pwd = input('请输入密码:')
        if user == 'alex' and pwd == 'sb':
            print('登录成功')
        else:
            print('登录失败')


obj = Account()
obj.login()
