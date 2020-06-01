import threading
import time

num = 100


def fun_sub():
    global num
    lock.acquire()
    print('----加锁----')
    print('现在操作共享资源的线程名字是:', t.name)
    num2 = num
    time.sleep(0.001)
    num = num2-1
    lock.release()
    print('----释放锁----')


if __name__ == '__main__':
    print('开始测试同步锁 at %s' % time.ctime())

    lock = threading.Lock()  # 创建一把同步锁

    thread_list = []
    for thread in range(100):
        t = threading.Thread(target=fun_sub)
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()  # 所有子线程都结束了, 主线程才结束
    print('num is %d' % num)
    print('结束测试同步锁 at %s' % time.ctime())
