from multiprocessing import Process
import os
import time

"""
新创建的进程与进程的切换都是要耗资源的，所以平时工作中进程数不能开太大。
同时可以运行的进程数一般受制于CPU的核数。
除了使用Process方法，我们还可以使用Pool类创建多进程。
"""

def long_time_task(i):
    print('子进程: {} - 任务{}'.format(os.getpid(), i))
    time.sleep(2)
    print("结果: {}".format(8 ** 20))


if __name__ == '__main__':
    print('当前母进程: {}'.format(os.getpid()))
    start = time.time()
    p1 = Process(target=long_time_task, args=(1,))
    p2 = Process(target=long_time_task, args=(2,))
    print('等待所有子进程完成。')
    p1.start()
    p2.start()
    p1.join()
    p2.join()  # 主进程阻塞, 等待子进程都完成任务才开始打印总耗时.
    end = time.time()
    print("总共用时{}秒".format((end - start)))

"""
下面介绍一下multiprocessing 模块下的Pool类的几个方法：
1.apply_async
函数原型：apply_async(func[, args=()[, kwds={}[, callback=None]]])
其作用是向进程池提交需要执行的函数及参数， 各个进程采用非阻塞（异步）的调用方式，即每个子进程只管运行自己的，不管其它进程是否已经完成。
这是默认方式。

2.map()
函数原型：map(func, iterable[, chunksize=None])
Pool类中的map方法，与内置的map函数用法行为基本一致，它会使进程阻塞直到结果返回。 注意：虽然第二个参数是一个迭代器，但在实际使用中，
必须在整个队列都就绪后，程序才会运行子进程。

3.map_async()
函数原型：map_async(func, iterable[, chunksize[, callback]])
与map用法一致，但是它是非阻塞的。其有关事项见apply_async。

4.close()
关闭进程池（pool），使其不在接受新的任务。

5. terminate()
结束工作进程，不在处理未处理的任务。

6.join()
主进程阻塞等待子进程的退出， join方法要在close或terminate之后使用。


"""