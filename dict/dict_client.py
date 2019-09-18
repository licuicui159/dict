"""
dict 客户端

功能: 发起请求,接收结果
"""
import getpass
from socket import *
import sys

# 服务器地址
ADDR=('127.0.0.1', 8888)


# 注册功能
def do_register(s):
    while True:
        name=input("User:")
        pwd=getpass.getpass()
        pwd1=getpass.getpass()
        if pwd != pwd1:
            continue
        if (' ' in name) or (' ' in pwd):
            print("用户名或密码不能含空格")
            continue

            msg="R %s %s " % (name, pwd)
            s.send(msg.encode())  # 发送请求
            data=s.recv(128).decode() # 反馈
            if data=='OK':
                print("注册成功")
            else:
                print("注册失败")


# 搭建网络
def main():
    s=socket()
    s.connect(ADDR)
    while True:
        print("""
        ========== Welcome ============
          1.注册     2.登录     3.退出
        ===============================
        """)
        cmd=input("选项(1,2,3):")
        s.send(cmd.encode())


if __name__ == '__main__':
    main()
