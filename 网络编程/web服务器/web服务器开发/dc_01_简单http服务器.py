import socket


def server_client(client_socket):
    """接收客户端请求，返回数据"""
    request = client_socket.recvfrom(1024)
    print(request)
    # 浏览器接收数据。现在至少两个\n
    response = "HTTP/1.1 200 OK\r\n\n"
    response += ""
    client_socket.send(response.encode("utf-8"))
    client_socket.close()


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close，即服务器4次挥手之后资源能够立即释放,程序运行后，重复使用这个端口资源
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server_socket.bind(("", 7780))
    tcp_server_socket.listen(128)
    while True:
        client_socket, client_add = tcp_server_socket.accept()
        server_client(client_socket)
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
