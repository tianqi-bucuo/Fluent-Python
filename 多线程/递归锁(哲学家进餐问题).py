from threading import RLock, Thread
import time
knife_lock = fork_lock = RLock()    # 设置为同一个锁


def eat1(name):
    knife_lock.acquire()
    print('%s拿到刀子' % name)
    fork_lock.acquire()
    print('%s拿到叉子' % name)
    print('%s eating' % name)
    fork_lock.release()
    knife_lock.release()


def eat2(name):
    fork_lock.acquire()
    print('%s拿到插子' % name)
    time.sleep(1)
    knife_lock.acquire()
    print('%s拿到刀子' % name)
    print('%s eating' % name)
    knife_lock.release()
    fork_lock.release()


Thread(target=eat1, args=('1',)).start()
Thread(target=eat2, args=('2',)).start()
Thread(target=eat1, args=('3',)).start()
Thread(target=eat2, args=('4',)).start()
