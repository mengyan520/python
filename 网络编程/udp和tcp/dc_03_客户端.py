from socket import  *
def main():
    tcp_client_socket =  socket(AF_INET, SOCK_STREAM)
    tcp_client_socket.connect(("127.0.0.1",7788))
    tcp_client_socket.send("哈哈".encode("gbk"))
    recv_data = tcp_client_socket.recv(1024)
    print("客户端接收的数据为：", recv_data.decode("gbk"))
    tcp_client_socket.close()

if __name__ == '__main__':
    main()
