def login():
    while True:
        print("\n=========Command==============")
        print("*****      查单词        *****")
        print("*****      记录        *****")
        print("*****      注销        *****")
        print("===============================")
        cmd = input("Command:")
        if cmd == "登录":
            pass
        elif cmd == '注销':
            break

while True:
    print("\n=========Command==============")
    print("*****      注册        *****")
    print("*****      登录        *****")
    print("*****      退出        *****")
    print("===============================")
    cmd = input("Command:")
    if cmd == "登录":
        login()
    elif cmd == '注册':
        login()
    elif cmd == '退出':
        break
