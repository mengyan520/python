import socket
import time

client_socket_list = list()


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setblocking(False)
    # 设置当服务器先close，即服务器4次挥手之后资源能够立即释放,程序运行后，重复使用这个端口资源
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server_socket.bind(("", 7788))
    tcp_server_socket.listen(128)
    while True:
        time.sleep(0.5)
        try:
            client_socket, client_add = tcp_server_socket.accept()
        except Exception as ret:
            print("没有新的客户端到来")
        else:
            print("来了新的客户端到来")
            client_socket.setblocking(False)
            client_socket_list.append(client_socket)
        for client_socket in client_socket_list:
            try:
                rev_content = client_socket.recv(1024)
            except Exception as ret:
                print("这个客户端没有发送数据")
            else:
                if rev_content:
                    print("发送过来数据：", rev_content)
                else:
                    print("移除client_socket")
                    client_socket_list.remove(client_socket)
                    client_socket.close()

    tcp_server_socket.close()


if __name__ == '__main__':
    main()
