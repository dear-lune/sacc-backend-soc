# 【小目标 5：说明选择理由】
# 选择 TCP 协议。因为题目只要求“发账号名，回 Hello World”这种点对点简单通信，
# TCP：可靠，面向连接，UDP：快，但不保证可靠，HTTP：浏览器和后端常用

import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.AF_INET：表示用 IPv4 地址（比如 127.0.0.1）。
#socket.SOCK_STREAM：表示用 TCP 协议（可靠传输，像水流一样稳定）。
    
    #本机地址和端口 8080
    server_socket.bind(("127.0.0.1", 8080))
    
    #开始监听
    server_socket.listen(5)
    print("服务端已启动，正在监听 8080 端口...")
    
    try:
        while True:
            # 等待客户端连接（会在这里卡住，直到有人连上来）
            client_socket, client_address = server_socket.accept()
            print(f"\n客户端 {client_address} 已连接")
            
            # 6. 接收客户端发来的数据（账号名）
            data = client_socket.recv(1024).decode("utf-8")
            print(f"收到请求内容: {data}") 
#recv(1024)：一次最多听 1024 个字节。它也会卡住，直到客户端真的发消息过来。
#.decode("utf-8")：收到的原始数据是“电信号”（字节），必须用 utf-8 解码成人类能看的字符串。
            
            # 返回内容 Hello World!
            response = "Hello World!"
            client_socket.sendall(response.encode("utf-8"))
            print(f"已返回响应: {response}")
            
            # 关闭与当前客户端的连接（但服务端不关，继续等下一个）
            client_socket.close()
            
    except KeyboardInterrupt:
        print("\n服务端手动停止。")
    finally:
        # 释放资源
        server_socket.close()

if __name__ == "__main__":
    start_server()