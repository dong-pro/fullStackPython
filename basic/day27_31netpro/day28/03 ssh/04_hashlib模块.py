import hashlib

md5 = hashlib.md5()
md5.update(b"hello")
md5.update(b"yuan")  # 追加

print(md5.hexdigest())
print(len(md5.hexdigest()))

# helloyuan:               d843cc930aa76f7799bba1780f578439
# 分开的hello，yuan:       d843cc930aa76f7799bba1780f578439

#############################################

md5 = hashlib.md5()

with open("02_ssh_client.py", "rb") as f:
    for line in f:
        md5.update(line)

print(md5.hexdigest())  # f.read()
