import threading
import time


class MyThread(threading.Thread):
    # 自动调用run方法
    def run(self):
        for i in range(3):
            time.sleep(1)
            # name：当前线程的名字
            msg = "I'm " + self.name + "@" + str(i)
            print(msg)

    def __del__(self):
        print("结束")


if __name__ == '__main__':
    t = MyThread()
    t.start()
