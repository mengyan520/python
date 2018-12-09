import socket
import re
import threading


def server_client(client_socket):
    """接收客户端请求，返回数据"""
    # 先解码
    request = client_socket.recv(1024).decode("utf-8")
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
        response = "HTTP/1.1 200 OK\r\n\n"
        # 发送响应头
        client_socket.send(response.encode("utf-8"))
    # 发送 body
    client_socket.send(html_content)
    client_socket.close()


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close，即服务器4次挥手之后资源能够立即释放,程序运行后，重复使用这个端口资源
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server_socket.bind(("", 7780))
    tcp_server_socket.listen(128)
    while True:
        client_socket, client_add = tcp_server_socket.accept()
        p = threading.Thread(target=server_client,args=(client_socket, ))
        p.start()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
