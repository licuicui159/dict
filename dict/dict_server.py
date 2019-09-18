"""
dict 服务端
* 处理业务逻辑
*多进程并发模型
"""

from socket import *
from multiprocessing import Process
import signal,sys
from threading import Thread

HOST='0.0.0.0'
PORT=8888
ADDR=(HOST,PORT)

# 注册逻辑
def do_register(connfd,data):
    tmp=data.split(' ')
    name=tmp[1]
    passwd=tmp[2]


# 客户端处理
def request(connfd):
    while True:
        data=connfd.recv(1024).decode() # 接收请求
        if data[0]=="R":
            do_register(connfd,data)
        print(data.decode())
        c.send(b'OK')
    c.close()

# 搭建网络
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(5)

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    # 循环等待客户端链接
    while True:
        print('Listen to port 8888')
        try:
            c,addr=sockfd.accept()
            print('Connect from',addr)
        except KeyboardInterrupt:
            sys.exit('服务退出')
        except Exception as e:
            print(e)
            continue
            # 创建线程
        t=Thread(target=request, args=(c,))
        t.setDaemon(True)
        t.start()


