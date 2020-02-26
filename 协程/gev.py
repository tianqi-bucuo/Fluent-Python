from gevent import monkey; monkey.patch_all()  # 使用monkey.patch_all()，gevent才会识别其他包的IO操作
import time
import gevent


def eat():
    print('eat')
    time.sleep(1)
    print('eat over')


def drink():
    print('drink')
    time.sleep(1)
    print('drink over')


g1 = gevent.spawn(eat)
g2 = gevent.spawn(drink)
g1.join()
g2.join()

