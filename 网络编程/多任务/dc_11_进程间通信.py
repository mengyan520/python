import multiprocessing


def down_data(q:multiprocessing.Queue):
    # 模拟下载数据
    data = [11, 22, 33]
    for temp in data:
        q.put(temp)
    print("下载完成,并存入到队列中")


def analysis_data(q:multiprocessing.Queue):
    # 数据处理
    waiting_datas = list()
    while True:
        data = q.get()
        waiting_datas.append(data)
        if q.empty():
            break
    print("读取数据：",waiting_datas)


def main():
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=down_data, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
