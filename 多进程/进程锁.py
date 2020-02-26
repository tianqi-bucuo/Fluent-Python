# 文件db的内容为：{"count":5}
# 注意一定要用双引号，不然json无法识别
# 并发运行，效率高，但竞争写同一文件，数据写入错乱
from multiprocessing import Process, Lock
import time,json,random


def search():
    dic = json.load(open('db'))
    print('\033[34m剩余票数%s\033[0m' % dic['count'])


def get(arg):
    dic = json.load(open('db'))
    time.sleep(0.2)  # 模拟读数据的网络延迟
    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(0.2)  # 模拟写数据的网络延迟
        json.dump(dic, open('db', 'w'))
        print('进程%s' % arg + '\033[32m购票成功\033[0m')
    else:
        print('进程%s' % arg + '\033[31m购票失败\033[0m')


def task(lock, arg):
    search()
    lock.acquire()  # 拿钥匙
    get(arg)
    lock.release()  # 还钥匙


if __name__ == '__main__':
    lock = Lock()
    for i in range(10):  # 模拟并发10个客户端抢票
        p = Process(target=task, args=(lock, i))
        p.start()

