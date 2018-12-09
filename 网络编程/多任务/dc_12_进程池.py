import multiprocessing
import os, time, random

def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d" % (msg, os.getpid()))
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print("%d执行完毕，耗时%0.2f" % (msg, t_stop - t_start))


def main():
    po = multiprocessing.Pool(3)
    for i in range(0, 10):
        # apply_async(调用目标,参数元组)
        # 每次循环将会用空闲出来的子进程去调用目标
        po.apply_async(worker, (i,))
    print("start")
    # 关闭进程池，关闭后不再接收新的请求
    po.close()
    # 主进程不会等待进程池执行完成
    # 等待po中所又子进程执行完成，必须放在close语句之后 ，进行堵塞
    po.join()

    print("end")


if __name__ == '__main__':
    main()
