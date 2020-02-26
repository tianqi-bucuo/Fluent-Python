from multiprocessing import Event

e = Event()    # 创建了一个事件，默认状态是False
print(e.is_set())    # 查看事件状态
e.set()    # 将事件状态改为True
print(e.is_set())
e.wait()    # 根据事件状态决定是否阻塞，True不阻塞，False阻塞，不wait不阻塞。
print('*'*10)
e.clear()   # 将事件状态改为False
print(e.is_set())
e.wait()    # 等待时间状态改为True
print('*'*10)

