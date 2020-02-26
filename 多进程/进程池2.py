import time
from multiprocessing import Pool
# 有返回值的进程池函数


def func(i):
    time.sleep(0.5)
    return i*i


if __name__ == '__main__':
    p = Pool(5)
    res_l = []
    for i in range(10):
        res = p.apply_async(func, args=(i,))
        res_l.append(res)
    for res in res_l:
        print(res.get())    # get方法获取res的返回值，不能放在上一个for里面，否则会改异步为同步
