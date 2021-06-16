import subprocess

# 第一个参数'ls'，需要区分不同的操作系统：Windows下面用dir，Mac下面用ls
# 编码方式：Windows下面用gbk，Mac下面用utf-8
res = subprocess.Popen('ls',
                       shell=True,
                       stderr=subprocess.PIPE,
                       stdout=subprocess.PIPE)

print(res.stdout.read().decode('utf-8'))