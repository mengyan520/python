import socket
import threading


def recv_msg():
    # 接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def send_msg():
    #  发送数据
    while True:
        send_data = input("请输入要发送的数据：")
        udp_socket.sendto(send_data.encode("utf-8"), ("", 7789))


def main():
    # 绑定本地信息
    udp_socket.bind(("", 7788))
    udp_socket.close()


# 创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
if __name__ == '__main__':
    main()
