from greenlet import greenlet

import time


def task1():
    while True:
        print("====1====")
        g2.switch()
        time.sleep(1)


def task2():
    while True:
        print("====2====")
        g1.switch()
        time.sleep(1)


g1 = greenlet(task1)
g2 = greenlet(task2)

g1.switch()
