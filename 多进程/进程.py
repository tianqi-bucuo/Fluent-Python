from multiprocessing import Process
import time
import os


def func(arg1, arg2):
    print('*'*arg1)
    time.sleep(2)
    print('子进程：', os.getpid())
    print('*'*arg2)


if __name__ == '__main__':  # windows系统中必须有这一行
    p = Process(target=func, args=(10, 20))  # 注册，args是传递参数的方式
    # p.daemon = True   # 设置子进程为守护进程，父进程结束后子进程自动结束
    p.start()  # 通知操作系统开启一个子进程
    print('########')
    p.join()    # 感知一个子进程的结束，将一个异步程序改为同步，join后的内容在p结束后才执行
    print('父进程:', os.getpid())
    print('父进程的父进程：', os.getppid())
    print('运行完了')

