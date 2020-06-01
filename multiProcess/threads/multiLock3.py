import threading
import time

"""
先说说为什么我们需要这个同步条件，我们的python多线程在执行task过程中，是相互竞争的，大家都可以先获取cpu的执行权限，这就是问题所在的地方，
每个线程都是独立运行且状态不可预测，但是我们想想如果我们的业务中需要根据情况来决定线程的执行顺序，
也就是程序中的其他线程需要通过判断某个线程的状态来确定自己下一步的操作，这时候我们就需要使用threading库中的Event对象。 
对象包含一个可由线程设置的信号标志,它允许线程等待某些事件的发生。
在 初始情况下,Event对象中的信号标志被设置为假，如果有线程等待一个Event对象, ,那么这个线程将会被一直阻塞直至该标志为真。
一个线程如果将一个Event对象的信号标志设置为真,它将唤醒所有等待这个Event对象的线程继续执行。


1.模拟1个老师和10个学生，进行考试，我们需要的目的是学生线程要等待老师线程说完“大家现在考试”，然后学生线程去考试，
之后老师线程说“考试结束”，学生线程放学回家，学生线程的执行与否取决于老师线程，所以这里用的Event
2.学生线程开始event.wait()，这个说明如果event如果一直不设置的话，学生线程就一直等待，等待一个event.set()操作
3.老师线程说完"大家现在要考试"，然后event.set()，执行event,设置完执行，学生线程就能够被唤醒继续执行下面的操作发出"啊啊啊啊啊啊"的叫苦连天
4.学生线程进行考试，并且执行event.clear()，清除event，因为他们在等老师说“考试结束”，之后他们在等老师线程的event.set()
5.老师线程执行event.set()，唤醒学生线程，然后下课回家.
"""


class Teacher(threading.Thread):
    def run(self):
        print("开始考试!")
        print(event.isSet())
        event.set()
        time.sleep(3)
        print("考试结束")
        print(event.isSet())
        event.set()


class Student(threading.Thread):
    def run(self):
        event.wait()
        print("正在做题 !")
        time.sleep(1)
        event.clear()
        event.wait()
        print("放学回家")


if __name__ == "__main__":
    event = threading.Event()
    threads = []
    for i in range(10):
        threads.append(Student())
    threads.append(Teacher())
    for t in threads:
        t.start()
    for t in threads:
        t.join()
