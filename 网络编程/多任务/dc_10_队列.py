from multiprocessing import  Queue


def main():
    q = Queue(3)
    q.put("消息1")
    q.put("消息2")
    print(q.full())
    q.put("消息3")
    print(q.get())
    print(q.get())
    print(q.get_nowait())
    print(q.get())
    print(q.empty())

if __name__ == '__main__':
    main()