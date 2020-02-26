from multiprocessing import Event, Process
import time
import random


def cars(e, i):
    if not e.is_set():
        print('car%s等待中' % i)
        e.wait()    # 阻塞，等待时间状态变为True
    print('car%s通过' % i)


def light(e):
    while True:
        if e.is_set():
            e.clear()
            print('\033[31m红灯\033[0m')
        else:
            e.set()
            print('\033[32m绿灯\033[0m')
        time.sleep(1)


if __name__ == '__main__':
    e = Event()
    traffic = Process(target=light, args=(e,))
    traffic.start()
    for i in range(20):
        car = Process(target=cars, args=(e, i))
        car.start()
        time.sleep(random.random())

