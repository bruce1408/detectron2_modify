import threading, time

"""
线程安全问题,list不是线程安全的
"""
m = [1, 2, 3, 4, 5]
print(m[-1])


def remove_last():
    a = m[-1]
    time.sleep(1)
    m.remove(a)


t1 = threading.Thread(target=remove_last)
t1.start()

t2 = threading.Thread(target=remove_last)
t2.start()
