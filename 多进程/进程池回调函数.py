import os
from multiprocessing import Pool


def func1(n):
    print('func1:', os.getpid())
    return n*n


def func2(n):
    print('func2:', os.getpid())    # 回调函数在主进程中执行
    print(n)


if __name__ == '__main__':
    print('主进程：', os.getpid())
    p = Pool(5)
    p.apply_async(func1, args=(10,), callback=func2)    # func1的返回值作为参数传给回调函数
    p.close()
    p.join()
