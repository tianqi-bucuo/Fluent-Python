import threading

semaphore = threading.BoundedSemaphore(1)


def func(num):
    semaphore.acquire()
    print("the number is: {}".format(num))
    semaphore.release()
    # 再次释放信号量，信号量加一，这是超过限定的信号量数目，这时会报错ValueError: Semaphore released too many times
    semaphore.release()


if __name__ == "__main__":
    num = 12
    th1 = threading.Thread(target=func, args=(num,))
    th1.start()
    th1.join()