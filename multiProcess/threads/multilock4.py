import threading
import time

"""
信号量用来控制线程并发数的，Semaphore管理一个内置的计数器，每当调用acquire()时-1，调用release()时+1。
计数器不能小于0，当计数器为0时，acquire()将阻塞线程至同步锁定状态，直到其他线程调用release()。
其实就是控制最多几个线程可以操作同享资源。

下面的例子就是创建10个线程，让每次只让5个线程去执行func函数。

结果：5个线程一批一批的执行打印,中间停格2s
"""
semaphore = threading.Semaphore(5)


def func():
    if semaphore.acquire():
        print(threading.currentThread().getName() + '获取共享资源')
        time.sleep(2)
        semaphore.release()


for i in range(10):
    t1 = threading.Thread(target=func)
    t1.start()
