import threading
import time


# 例子 1
# def long_time_task(i):
#     print('当前子线程: {} - 任务{}'.format(threading.current_thread().name, i))
#     time.sleep(4)
#     print("结果: {}".format(8 ** 20))
#
#
# """
# 为什么总耗时居然是0秒? 我们可以明显看到主线程和子线程其实是独立运行的，主线程根本没有等子线程完成，而是自己结束后就打印了消耗时间。
# 主线程结束后，子线程仍在独立运行，这显然不是我们想要的。
# """
# if __name__ == '__main__':
#     start = time.time()
#     print('这是主线程：{}'.format(threading.current_thread().name))
#     t1 = threading.Thread(target=long_time_task, args=(1,))
#     t2 = threading.Thread(target=long_time_task, args=(2,))
#     t1.start()
#     t2.start()
#
#     end = time.time()
#     print("总共用时{}秒".format((end - start)))


# 例子 2
# def long_time_task(i):
#     print('当前子线程: {} 任务{}'.format(threading.current_thread().name, i))
#     time.sleep(2)
#     print("结果: {}".format(8 ** 20))
#
#
# """
# 当我们设置多线程时，主线程会创建多个子线程，在python中，默认情况下主线程和子线程独立运行互不干涉。
# 如果希望让主线程等待子线程实现线程的同步，我们需要使用join()方法。如果我们希望一个主线程结束时不再执行子线程，
# 我们应该怎么办呢? 我们可以使用t.setDaemon(True),守护子线程
# """
#
# if __name__ == '__main__':
#     start = time.time()
#     print('这是主线程：{}'.format(threading.current_thread().name))
#     thread_list = []
#     for i in range(1, 3):
#         t = threading.Thread(target=long_time_task, args=(i,))
#         thread_list.append(t)
#
#     for t in thread_list:
#         t.start()
#
#     for t in thread_list:
#         t.join()
#
#     end = time.time()
#     print("总共用时{}秒".format((end - start)))


# 例子 3
def long_time_task():
    print('当子线程: {}'.format(threading.current_thread().name))
    time.sleep(2)
    print("结果: {}".format(8 ** 20))


if __name__ == '__main__':
    start = time.time()
    print('这是主线程：{}'.format(threading.current_thread().name))
    for i in range(5):
        t = threading.Thread(target=long_time_task, args=())
        t.setDaemon(True)  # 就是守护子进程
        t.start()

    end = time.time()
    print("总共用时{}秒".format((end - start)))
