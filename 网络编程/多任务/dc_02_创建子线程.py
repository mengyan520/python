import threading
import time


def sing():
    for i in range(5):
        print("---唱歌----")
        time.sleep(1)


def dance():
    for i in range(5):
        print("---跳舞----")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    # 创建并启动线程
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
