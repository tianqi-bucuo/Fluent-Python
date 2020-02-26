from threading import Thread, Lock
import time


def func(lock):
    global n
    lock.acquire()
    temp = n
    time.sleep(1)
    n = temp - 1
    lock.release()


n = 10
t_list = []
lock = Lock()
for i in range(10):
    t = Thread(target=func, args=(lock,))
    t.start()
    t_list.append(t)

for t in t_list:
    t.join()
print(n)

