"""
dict 客户端

功能: 发起请求,接收结果
"""
import sys
from socket import *
import getpass

# 服务器地址
ADDR=('127.0.0.1', 8888)
s=socket()
s.connect(ADDR)


# 注册功能
def do_register():
    while True:
        name=input("User:")
        pwd=getpass.getpass()
        pwd1=getpass.getpass("Again:")
        if pwd != pwd1:
            print("两次密码不一致！")
            continue
        if (' ' in name) or (' ' in pwd):
            print("用户名或密码不能含有空格")
            continue

        msg="R %s %s" % (name, pwd)
        s.send(msg.encode())  # 发送请求
        data=s.recv(128).decode()  # 反馈
        if data == 'OK':
            print("注册成功")
            login(name)
        else:
            print("注册失败")
        return


# 登录功能
def do_login():
    while True:
        name=input("User:")
        pwd=getpass.getpass("Pwd:")

        msg="L %s %s" % (name, pwd)
        s.send(msg.encode())  # 发送请求
        data=s.recv(128).decode()  # 反馈
        if data == 'OK':
            print("登录成功")
            login(name)
        else:
            print("登录失败")
        return


# 查单词功能
def do_query(name):
    while True:
        word=input("Word:")

        if word == '##':
            break
        msg="Q %s %s" % (name, word)
        s.send(msg.encode())  # 发送请求

        # 得到结果
        data=s.recv(2048).decode()  # 反馈
        print(data)


# 历史记录
def do_history(name):
    msg="H " + name
    s.send(msg.encode())  # 发送请求
    while True:
        data=s.recv(1024).decode()  # 反馈
        if data == '##':
            break
        print(data)

# 注销用户
def do_cancellation(name):
    msg="C " + name
    s.send(msg.encode())  # 发送请求
    data=s.recv(128).decode()  # 反馈
    if data == 'OK':
        print("注销成功")
    else:
        print("注销失败")
    return


# 二级界面
def login(name):
    while True:
        print("""
        ==========  Query  ============
         1.查单词  2.记录  3.注销  b.返回
        ===============================
        """)
        cmd=input("选项(1,2,3):")
        if cmd == "1":
            do_query(name)
        elif cmd == '2':
            do_history(name)
        elif cmd == '3':
            do_cancellation(name)
        elif cmd == 'b':
            break
        else:
            print("请输入正确命令")


# 搭建网络
def main():
    while True:
        print("""
        ========== Welcome ============
          1.注册     2.登录     q.退出
        ===============================
        """)
        cmd=input("选项(1,2,3):")
        if cmd == '1':
            do_register()
        elif cmd == '2':
            do_login()
        elif cmd == 'q':
            s.send(b'E')
            sys.exit("谢谢使用")
        else:
            print("请输入正确的选项")


if __name__ == '__main__':
    main()
