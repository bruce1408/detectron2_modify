import threading
import time

num = 100

"""
锁通常被用来实现对共享资源的同步访问。为每一个共享资源创建一个Lock对象，当你需要访问该资源时，调用acquire方法来获取锁对象
（如果其它线程已经获得了该锁，则当前线程需等待其被释放），待资源访问完后，再调用release方法释放锁
"""


def fun_sub():
    global num
    # num -= 1
    num2 = num
    time.sleep(0.001)
    num = num2-1


if __name__ == '__main__':
    print('开始测试同步锁 at %s' % time.ctime())

    thread_list = []
    for thread in range(100):
        t = threading.Thread(target=fun_sub)
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()
    print('num is %d' % num)
    print('结束测试同步锁 at %s' % time.ctime())
