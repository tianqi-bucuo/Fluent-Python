from multiprocessing import Process, Semaphore
import time


def func(i, sem):
    sem.acquire()   # 拿钥匙
    print('进程%s开始执行' % i)
    time.sleep(5)
    print('进程%s执行结束' % i)
    sem.release()   # 还钥匙


if __name__ == '__main__':
    sem = Semaphore(4)  # 设置4把钥匙
    for i in range(20):
        p = Process(target=func, args=(i, sem))
        p.start()
