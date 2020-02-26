from multiprocessing import Process
import time


def func(arg):
    print('进程%s开始' % arg)
    time.sleep(1)
    print('进程%s结束' % arg)


if __name__ == '__main__':
    p_list = []
    for i in range(5):
        p = Process(target=func, args=(i,))
        p.start()
        p_list.append(p)
    for p in p_list:  # 所有子进程结束后再执行后面的父进程
        p.join()
    print('主进程结束')
