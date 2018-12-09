import socket
import re
import select


client_socket_list = list()


def server_client(client_socket,request):
    """接收客户端请求，返回数据"""
    # 先解码
    # request = client_socket.recv(1024).decode("utf-8")
    print("========" * 50)
    # 切割请求数据
    request_lines = request.splitlines()
    # print(request_lines)
    # 获取文件名 'GET /index.html HTTP/1.1'
    # 这个正则的意思是
    # [^/]+:代表取到不是 / ，至少有一个
    # /[^ ]*：代表取到不是 空格，有或没有
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    file_name = ""
    if ret:
        file_name = ret.group(1)
        print(file_name)
        if file_name == "/":
            file_name = "/index.html"

    try:
        f = open("./京东案例" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n\n"
        response += "not found"
        client_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        # 浏览器接收数据。现在至少两个\n
        response_body = html_content
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"
        # 发送响应头
        response = response_header.encode("utf-8 ") + response_body
        client_socket.send(response)


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close，即服务器4次挥手之后资源能够立即释放,程序运行后，重复使用这个端口资源
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server_socket.bind(("", 7780))
    tcp_server_socket.listen(128)
    # 将套接字变为非堵塞
    tcp_server_socket.setblocking(False)
    # 创建一个epoll对象
    epl = select.poll()
    # 将监听套接字对应的fd注册到epoll中
    epl.register(tcp_server_socket.fileno(), select.POLLIN)
    fd_event_dict = dict()
    while True:
        # 默认堵塞，直到os检测数据到来，以通知的形式告诉程序，才会解堵塞
        # [(fd,event),]
        fd_event_list = epl.poll()
        for fd,event in fd_event_list:
            if fd == tcp_server_socket.fileno():
                client_socket, client_add = tcp_server_socket.accept()
                epl.register(client_socket.fileno(), select.POLLIN)
                fd_event_dict[client_socket.fileno()] = client_socket
            elif event == select.POLLIN:
                # 判断已连接的客户端发送数据
                new_socket = fd_event_dict[fd]
                rev_content = new_socket.recv(1024).decode("utf-8")
                if rev_content:
                    # print("发送过来数据：", rev_content)
                    server_client(new_socket, rev_content)
                else:
                    print("移除client_socket")
                    new_socket.close()
                    epl.unregister(fd)
                    fd_event_dict.pop(fd)
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
