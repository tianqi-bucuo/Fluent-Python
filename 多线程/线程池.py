import time
from concurrent.futures import ThreadPoolExecutor
# from concurrent.futures import ProcessPoolExecutor    # 进程池用法与线程池完全相同


def func(n):
    time.sleep(0.5)
    print(n)
    return n*n


t_pool = ThreadPoolExecutor(max_workers=5)  # 一般不超过CPU*5
t_list = []
for i in range(20):
    t = t_pool.submit(func, i)
    t_list.append(t)
t_pool.shutdown()   # close()+join()
print('主线程')
for t in t_list:
    print(t.result())
