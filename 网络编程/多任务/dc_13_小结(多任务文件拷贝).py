import os
import multiprocessing
import time


def copy_file(file_name, old_folder_name, new_folder_name, queue):
    """文件拷贝"""
    # 读取源文件
    old_file = open(old_folder_name + "/" + file_name, "rb")
    content = old_file.read()
    old_file.close()
    # 写入新文件
    new_file = open(new_folder_name + "/" + file_name, "wb")
    new_file.write(content)
    new_file.close()
    # 发送已经拷贝完毕的文件名字 queue = multiprocessing.Manager().Queue()
    queue.put(file_name)


def main():
    # 获取用户要拷贝的文件夹的名字
    old_folder_name = input("请输入要拷贝的文件夹的名字：")
    # 创建一个新的文件夹
    try:
        new_folder_name = old_folder_name + "复制"
        os.mkdir(new_folder_name)
    except:
        pass
    # 获取文件夹所有的待拷贝的文件名字  os.listdir
    file_names = os.listdir(old_folder_name)
    # 创建队列
    queue = multiprocessing.Manager().Queue()
    # 创建进程池
    po = multiprocessing.Pool(5)
    # 向进程池中添加拷贝文件任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(file_name, old_folder_name, new_folder_name, queue))
    po.close()
    # po.join()
    # 显示进度
    all_file_num = len(file_names)
    while True:
        file_name = queue.get()
        print("已经完成copy：",file_name)
        if file_name in file_names:
            file_names.remove(file_name)
        copy_rate = ((all_file_num - len(file_names)) * 100 / all_file_num)
        print("\r%.2f...(%s)" % (copy_rate, file_name))
        if copy_rate >= 100:
            break


if __name__ == '__main__':
    main()
