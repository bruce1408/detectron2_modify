from multiprocessing import Process
import os

"""
父进程启动,同时,启动子进程并等待结束.
"""

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('child',))
    p.start()  # 启动进程
    p.join()  # 实现进程之间的通信和同步,等待所有进程退出 close()阻止多余进程涌入进程池pool造成堵塞
    print('End')