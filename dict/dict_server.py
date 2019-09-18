"""
dict 服务端

* 处理业务逻辑
* 多进程并发模型
"""

from socket import *
from multiprocessing import Process
import signal, sys
from time import sleep
from dict_db import User

HOST='0.0.0.0'
PORT=8888
ADDR=(HOST, PORT)
db=User(database='dict')  # 数据库操作对象


# 注册逻辑
def do_register(connfd, data):
    tmp=data.split(' ')
    name=tmp[1]
    passwd=tmp[2]
    if db.register(name, passwd):
        connfd.send(b'OK')
    else:
        connfd.send(b'Fail')

# 登录功能
def do_login(connfd, data):
    tmp=data.split(' ')
    name=tmp[1]
    passwd=tmp[2]
    if db.login(name, passwd):
        connfd.send(b'OK')
    else:
        connfd.send(b'Fail')

# 查单词功能
def do_query(connfd, data):
    tmp=data.split(' ')
    name=tmp[1]
    word=tmp[2]

    # 单词查找
    mean=db.query(word)
    if not mean:
        connfd.send("没有找到该单词".encode())
    else:
        db.insert_history(name,word)
        msg="%s:%s" % (word,mean)
        connfd.send(msg.encode())

# 历史记录
def do_history(connfd, data):
    name=data.split(' ')[1]
    r=db.history(name)
    if not r[0]:
        connfd.send("没有记录".encode())
    for i in r:
        msg="%s  %-16s  %s" % i
        connfd.send(msg.encode())
        sleep(0.1)
    connfd.send(b'##')

def do_cancellation(connfd, data):
    name=data.split(' ')[1]
    if db.cancellation(name):
        connfd.send(b'OK')
    else:
        connfd.send(b'Fail')

# 处理客户端各种请求
def request(connfd):
    db.create_cursor()  # 每个子进程有自己的游标
    while True:
        data=connfd.recv(1024).decode()  # 接受请求
        if not data or data[0] == 'E':
            sys.exit()
        elif data[0] == 'R':
            do_register(connfd, data)
        elif data[0] == 'L':
            do_login(connfd, data)
        elif data[0] == 'Q':
            do_query(connfd, data)
        elif data[0] == 'H':
            do_history(connfd, data)
        elif data[0] == 'C':
            do_cancellation(connfd, data)

# 搭建网络
def main():
    # 创建套接字
    s=socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    # 处理僵尸进场
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    # 循环等待客户端链接
    print("Listen the port 8888")
    while True:
        try:
            c, addr=s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            sys.exit("服务退出")
        except Exception as e:
            print(e)
            continue

        # 创建子进程
        p=Process(target=request, args=(c,))
        p.daemon=True
        p.start()


if __name__ == '__main__':
    main()
