import threading
import time

"""
守护子线程

join()：在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
setDaemon(True)：
将线程声明为守护线程，必须在start() 方法调用之前设置， 如果不设置为守护线程程序会被无限挂起。这个方法基本和join是相反的。
当我们在程序运行中，执行一个主线程，如果主线程又创建一个子线程，主线程和子线程 就分兵两路，分别运行，那么当主线程完成
想退出时，会检验子线程是否完成。如果子线程未完成，则主线程会等待子线程完成后再退出。但是有时候我们需要的是只要主线程
完成了，不管子线程是否完成，都要和主线程一起退出，这时就可以用setDaemon方法啦



GIL:全局解释器锁  无论你启多少个线程，你有多少个cpu, Python在执行的时候只会的在同一时刻只允许一个线程（线程之间有竞争）
拿到GIL在一个cpu上运行，当线程遇到IO等待或到达者轮询时间的时候，cpu会做切换，把cpu的时间片让给其他线程执行，
cpu切换需要消耗时间和资源，所以计算密集型的功能（比如加减乘除）不适合多线程，因为cpu线程切换太多，IO密集型比较适合多线程。

任务：
IO密集型（各个线程都会都各种的等待，如果有等待，线程切换是比较适合的），也可以采用可以用多进程+协程
计算密集型（线程在计算时没有等待，这时候去切换，就是无用的切换），python不太适合开发这类功能

"""


def say(name):
    print('你好%s at %s' % (name, time.ctime()))
    time.sleep(2)
    print("结束%s at %s" % (name, time.ctime()))


def listen(name):
    print('你好%s at %s' % (name, time.ctime()))
    time.sleep(4)
    print("结束%s at %s" % (name, time.ctime()))


if __name__ == '__main__':
    t1 = threading.Thread(target=say, args=('tony',))  # Thread是一个类，实例化产生t1对象，这里就是创建了一个线程对象t1
    # t1.setDaemon(True)
    t1.start()  # 线程执行
    t2 = threading.Thread(target=listen, args=('simon',))  # 这里就是创建了一个线程对象t2
    t2.setDaemon(True)
    t2.start()

    print("程序结束=====================")
