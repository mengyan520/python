import threading
import time

g_num = 0


def sing(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("sing== ",g_num)


def dance(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("dance== ",g_num)



def main():
    t1 = threading.Thread(target=sing,args=(1000000,))
    t2 = threading.Thread(target=dance,args=(1000000,))
    t1.start()
    t2.start()
    time.sleep(5)
    print("main==",g_num)


if __name__ == '__main__':
    main()
