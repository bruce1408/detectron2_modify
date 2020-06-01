from multiprocessing import Pool, cpu_count
import os
import time

"""
对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()或terminate()方法，让其不再接受新的Process了
"""


def long_time_task(i):
    print('子进程: {} - 任务{}'.format(os.getpid(), i))
    time.sleep(2)
    print("结果: {}".format(8 ** 20))


if __name__ == '__main__':
    print("CPU内核数:{}".format(cpu_count()))
    print('当前主进程: {}'.format(os.getpid()))
    start = time.time()
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('等待所有子进程完成。')
    p.close()  # 关闭进程池（pool），使其不在接受新的任务。
    p.join()  # 主进程阻塞等待子进程的退出， join方法要在close或terminate之后使用。
    end = time.time()
    print("总共用时{}秒".format((end - start)))
