import threading
import random

semaphore = threading.Semaphore(0)  # 信号量个数，默认值为1。


def producer():
    global item
    item = random.randrange(1, 1000)
    semaphore.release()  # 信号量的 release() 可以提高计数器然后通知其他的线程, 信号量个数增加+1
    print("producer notify : produced item number %s" % item)


def consumer():
    print("consumer is waiting....")
    global item
    semaphore.acquire(timeout=3)  # 信号量个数减1
    # 如果信号量的计数器到了0，就会阻塞 acquire() 方法，
    # 直到得到另一个线程的通知。如果信号量的计数器大于0，就会对这个值-1然后分配资源。
    print("consume notify : consume item number %s" % item)


if __name__ == "__main__":
    for i in range(3):
        th1 = threading.Thread(target=producer)
        th2 = threading.Thread(target=consumer)
        th1.start()
        th2.start()
        th1.join()
        th2.join()
    print("teminated")
