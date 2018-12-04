from socket import *


def main():
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)
    tcp_client_socket.connect(("127.0.0.1", 7788))
    # 输入想要下载的文件
    file_name = input("请输入下载的文件：")
    tcp_client_socket.send(file_name.encode("gbk"))
    # 保存文件
    recv_data = tcp_client_socket.recv(1024*1024)
    print(recv_data)
    if recv_data:
        with open("[新]"+"1111.py","w") as file:
            file.write(recv_data)
    tcp_client_socket.close()


if __name__ == '__main__':
    main()
