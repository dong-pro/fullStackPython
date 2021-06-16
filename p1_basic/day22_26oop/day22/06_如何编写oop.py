class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def file_read(self):
        pass

    def file_update(self):
        pass

    def file_delete(self):
        pass

    def file_add(self):
        pass


class Excel:
    def __init__(self, file_path):
        self.file_path = file_path

    def excel_read(self):
        pass

    def excel_update(self):
        pass

    def excel_delete(self):
        pass

    def excel_add(self):
        pass


class Person:
    def __init__(self, na, gen, age, fig):
        self.name = na
        self.gender = gen
        self.age = age
        self.fight = fig

    def grassland(self):
        self.fight = self.fight - 10

    def practice(self):
        self.fight = self.fight + 90

    def incest(self):
        self.fight = self.fight - 666

cang = Person('苍井井', '女', 18, 1000)  # 创建苍井井角色
dong = Person('东尼木木', '男', 20, 1800)  # 创建东尼木木角色
bo = Person('波多多', '女', 19, 2500)  # 创建波多多角色

dong.grassland()
