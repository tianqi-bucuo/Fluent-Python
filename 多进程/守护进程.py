from multiprocessing import Process
import time
# 守护进程会等主进程的代码执行完之后自动结束，(代码执行完即可，不一定等到主进程结束)


def func():
    while True:
        time.sleep(0.5)
        print('子进程')


if __name__ == '__main__':
    p1 = Process(target=func)
    p1.daemon = True  # 在p.start()之前，设置子进程为守护进程
    p1.start()
    # print(p.name, p.pid)  # 进程名和进程id
    # print(p.is_alive())  # 检验进程是否还活着
    # p.terminate()  # 结束子进程

    i = 0
    while i < 5:
        print('主进程执行中')
        time.sleep(1)
        i += 1
