# 创建线程的两种方式与创建进程相同，不再重复
from threading import Thread
import time
# 守护进程会随着主进程代码执行完后就结束
# 守护线程则会在主线程结束之后并且等待其他子线程结束后才结束


def func1():
    while True:
        print('func1')
        time.sleep(1)


def func2():
    while True:
        print('func2')
        time.sleep(1)


t1 = Thread(target=func1,)
t1.daemon = True
t1.start()
t2 = Thread(target=func2,)
t2.start()
print('主线程')



