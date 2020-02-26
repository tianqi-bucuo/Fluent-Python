f = open('file', 'r+', encoding='utf-8')
r1 = f.read()
f.seek(4)   # 按照字节定位光标
print(f.tell())    # 光标的位置
r2 = f.read()
line = f.readline()  # 读一行
print(line)
line_list = f.readlines()  # 返回一个列表
print(r1)
print(r2)
# 逐行读取
for line in f:
    print(line)

f.close()

