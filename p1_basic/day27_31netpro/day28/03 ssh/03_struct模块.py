import struct

res = struct.pack("i", 2143)

print(res)
print(len(res))

obj = struct.unpack("i", res)
print(obj[0])
print(obj)
