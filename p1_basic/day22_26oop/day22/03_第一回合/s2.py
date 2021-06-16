class Message:
    def email(self, em, text):
        """
        发送邮件
        :return:
        """
        print(em, text)

    def msg(self, tel, text):
        """
        发送短信
        :return:
        """
        print(tel, text)

    def wechat(self, num, text):
        """
        发送微信
        :return:
        """
        print(num, text)


# 编写功能:假设用户购买课程,然后给alex发送提醒;
if 1 == 1:
    obj = Message()
    obj.email('alex@sb.com', '张进购买了一个学位课')
    obj.msg('188888888', '张进购买了一个学位课')
    obj.wechat('xxxx', '张进购买了一个学位课')
