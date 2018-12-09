from socket import *


def main():
    # 创建套接字
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    # 绑定本地端口
    address = ("", 8080)
    tcp_server_socket.bind(address)
    tcp_server_socket.listen(128)
    # 接收多个客户端
    while True:
        client_socekt, client_addr = tcp_server_socket.accept()
        while True:
            # 接收客户端数据
            recv_data = client_socekt.recv(1024)

            # 客户端退出
            if recv_data:
                print("接收数据为：", recv_data.decode("gbk"))
            else:
                break
            # 发送数据到客户端
            client_socekt.send("HTTP/1.1 200 OK\r\n\n ghahahha".encode("gbk"))
        client_socekt.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
