import threading
import time

""""
上面代码中加入join方法后实现了，我们上面所想要的结果，主线程print最后执行，并且主线程退出，
注意主线程执行了打印操作和主线程结束不是一个概念，如果子线程不加join，则主线程也会执行打印，
但是主线程不会结束，还是需要待非守护子线程结束之后，主线程才结束。
上面的情况，主进程都需要等待非守护子线程结束之后，主线程才结束。
那我们是不是注意到一点，我说的是“非守护子线程”，那什么是非守护子线程？默认的子线程都是主线程的非守护子线程，
但是有时候我们有需求，当主进程结束，不管子线程有没有结束，子线程都要跟随主线程一起退出，这时候我们引入一个“守护线程”的概念。
默认的子线程都是主线程的非守护子线程

如果某个子线程设置为守护线程，主线程其实就不用管这个子线程了，当所有其他非守护线程结束，主线程就会退出，
而守护线程将和主线程一起退出，守护主线程，这就是守护线程的意思
"""


def say(name):
    print('你好%s at %s' % (name, time.ctime()))
    time.sleep(4)
    print("结束%s at %s" % (name, time.ctime()))


def listen(name):
    print('你好%s at %s' % (name, time.ctime()))
    time.sleep(1)
    print("结束%s at %s" % (name, time.ctime()))


if __name__ == '__main__':
    t1 = threading.Thread(target=say, args=('tony',))  # Thread是一个类，实例化产生t1对象，这里就是创建了一个线程对象t1
    t1.start()  # 线程执行
    t2 = threading.Thread(target=listen, args=('simon',))  # 这里就是创建了一个线程对象t2
    t2.start()

    t1.join()  # join等t1子线程结束，主线程打印并且结束
    t2.join()  # join等t2子线程结束，主线程打印并且结束
    print("程序结束=====================")
