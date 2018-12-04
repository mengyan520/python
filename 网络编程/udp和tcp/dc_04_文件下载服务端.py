from socket import *


def main():
    # 创建套接字
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    # 绑定本地端口
    address = ("", 7788)
    tcp_server_socket.bind(address)
    tcp_server_socket.listen(128)
    # 接收客户端
    while True:
        client_socekt, client_addr = tcp_server_socket.accept()
        # 接收客户端要下载的文件名
        file_name = client_socekt.recv(1024)
        # 客户端退出
        if file_name:
            print("接收数据为：", file_name.decode("utf-8"))

        # 发送文件到客户端
        file_content = None
        try:
            f = open(file_name.decode("utf-8"), "rb")
            file_content = f.read()
            f.close()
        except Exception as result:
            print("打开文件失败,没有要下载的文件,报错为：", result)
        if file_content:
            client_socekt.send(file_content)

    client_socekt.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
