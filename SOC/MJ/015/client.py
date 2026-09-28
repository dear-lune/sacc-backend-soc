import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # 连接服务端（IP 和 端口必须和服务端一致）
        client_socket.connect(("127.0.0.1", 8080))
        print("已成功连接到服务端。")
        
        # 发送请求
        account_name = input("请输入要创建的账号名: ")
        client_socket.sendall(account_name.encode("utf-8"))
        
        # 接收服务端返回的数据
        response = client_socket.recv(1024).decode("utf-8")
        print(f"收到服务端响应: {response}")
        
    except ConnectionRefusedError:
        print("连接失败：服务端未启动，或端口不正确。")
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        #关闭连接，释放资源
        client_socket.close()

if __name__ == "__main__":
    start_client()