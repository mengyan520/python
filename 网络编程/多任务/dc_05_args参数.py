import threading
import time

num_list = [11, 22]


def sing(temp):
    temp.append(33)
    print(temp)
    for i in range(5):
        print("---唱歌----")
        time.sleep(1)


def dance():
    for i in range(5):
        print("---跳舞----")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing, args=(num_list,))
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    print(num_list)


if __name__ == '__main__':
    main()
