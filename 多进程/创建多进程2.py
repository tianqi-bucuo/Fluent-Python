import os
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, arg1, arg2):  # 传递参数的方式
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2

    def run(self):  # 重写run方法
        print(os.getpid())
        print(self.arg1)
        print(self.arg2)


if __name__ == '__main__':
    print('主进程：', os.getpid())
    p1 = MyProcess(1, 2)
    p1.start()
    p2 = MyProcess(3, 4)
    p2.start()
