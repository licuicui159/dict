"""
dict 客户端

功能: 发起请求,接收结果
"""

from socket import *
import sys

# 服务器地址
ADDR = ('127.0.0.1',8888)

# 搭建网络
def main():
    s = socket()
    s.connect(ADDR)
    while True:
        print("""
        ========== Welcome ============
          1.注册     2.登录     3.退出
        ===============================
        """)
        cmd = input("选项(1,2,3):")
        s.send(cmd.encode())

if __name__ == '__main__':
    main()
