import os
import time
from multiprocessing import Pool


def func(n):
    print("start func%s" % n, os.getpid())
    time.sleep(1)
    print("end func%s" % n, os.getpid())


if __name__ == '__main__':
    p = Pool(5)
    for i in range(10):
        # p.apply(func, args=(i,))      # 同步执行
        p.apply_async(func, args=(i,))  # 异步执行
    p.close()   # 结束进程池接受任务
    p.join()    # 感知进程池中的任务执行结束
